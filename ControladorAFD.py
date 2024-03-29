from AFD import *
from Grafica import Grafica

class ControladorAFD:
    def __init__(self):
        self.automatas = []
        self.linea = 0

    def sacarLinea(self):
        try:
            return self.entrada.pop(0)
        except:
            return None

    def verLinea(self):
        try:
            return self.entrada[0]
        except:
            return None

    def identificarElementos(self):
        if self.linea == 0:
            self.automata = AFD()
            self.automata.nombreAFD = self.sacarLinea()
        elif self.linea == 1:
            self.automata.estados = self.sacarLinea().split(',')
            for estado in self.automata.estados:
                self.automata.path[estado] = {}
        elif self.linea == 2:
            self.automata.alfabeto = self.sacarLinea().split(',')
        elif self.linea == 3:
            self.automata.eInicial = self.sacarLinea()
        elif self.linea == 4:
            self.automata.eAceptacion = self.sacarLinea().split(',')
        elif self.linea == 5:
            self.transiciones = []
        if self.linea >= 5:
            transicion = self.sacarLinea().split(';')
            origenEntrada = transicion[0].split(',')
            self.transiciones.append(Transicion(origenEntrada[0],origenEntrada[1],transicion[1]))
            try:
                self.automata.path[origenEntrada[0]][origenEntrada[1]] = transicion[1]
            except: pass
        self.linea += 1
        if self.verLinea() == '%' or not self.verLinea():
            self.automata.transiciones = self.transiciones
            self.automatas.append(self.automata)
            self.sacarLinea()
            self.linea = 0
        if self.verLinea():
            self.identificarElementos()

    def agregarAFD(self,nombre,estados,alfabeto,eInicial,eAcept,transiciones,path):
        trans = []
        automata = AFD()
        automata.nombreAFD = nombre
        automata.estados = estados.split(';')
        automata.alfabeto = alfabeto.split(';')
        automata.eInicial = eInicial
        automata.eAceptacion = eAcept.split(';')

        for i in transiciones:
            valor = i.split(',')
            trans.append(Transicion(valor[0],valor[1],valor[2]))

        if not self.esDeterminista(trans):
            return False

        automata.transiciones = trans
        automata.path = path

        self.automatas.append(automata)
        return True

    def esDeterminista(self,transiciones):
        for i in range(len(transiciones)):
            for j in range(len(transiciones)):
                if i != j and transiciones[j].origen == transiciones[i].origen and transiciones[j].entrada == transiciones[i].entrada and transiciones[j].destino != transiciones[i].destino:
                    return False
        return True

    def cadenaMinima(self,cadenas,path,estado,acept,alf,cadena,cont) -> list:
        if cont > 20:
            return
        if estado in acept:
            cadenas.append(cadena)
            return
        destinos = path[estado]
        if len(cadenas) > 90:
            return
        for entrada in alf:
            try:
                self.cadenaMinima(cadenas,path,destinos[entrada],acept,alf,cadena + entrada,cont + 1)
            except: pass
        return cadenas

    def generarReporte(self,indice):
        automata = self.automatas[indice]
        cadenas = self.cadenaMinima([],automata.path,automata.eInicial,automata.eAceptacion,automata.alfabeto,'',1)
        try:
            cadenas.sort(key = len)
            cadena = cadenas[0]
        except:
            cadena = '$'
        Grafica().generarDotAFD(automata,cadena)

    # validando cadena
    def existeTransicion(self,entrada,transiciones):
        for transicion in transiciones:
            if entrada == transicion:
                return True
        return False

    def evaluarVacio(self,estado,aceptados):
        if estado in aceptados:
            return True, []
        return False

    def evaluarCaracteres(self,path,ruta,estado,aceptados,cadena,i):
        transiciones = path[estado]
        if i < len(cadena):
            if self.existeTransicion(cadena[i],transiciones):
                ruta.append([cadena[i],transiciones[cadena[i]]])
                if i == len(cadena) -1 and transiciones[cadena[i]] in aceptados:
                    return True, ruta
                return self.evaluarCaracteres(path,ruta,transiciones[cadena[i]],aceptados,cadena,i + 1)
        return False

    def validarCadena(self,cadena,indice):
        if len(cadena) > 0:
            return self.evaluarCaracteres(self.automatas[indice].path,[],self.automatas[indice].eInicial,self.automatas[indice].eAceptacion,cadena,0)
        return self.evaluarVacio(self.automatas[indice].eInicial,self.automatas[indice].eAceptacion)

    def generarRuta(self,cadena,indice):
        valido = self.validarCadena(cadena,indice)
        if valido:
            Grafica().generarRuta(self.automatas[indice].nombreAFD,valido[1],self.automatas[indice].eInicial)

    #-------
    def verAutomatas(self):
        for i in range(len(self.automatas)):
            print(f'Nombre: {self.automatas[i].nombreAFD}')
            print(f'Estados: {self.automatas[i].estados}')
            print(f'Alfabeto: {self.automatas[i].alfabeto}')
            print(f'Estados de Aceptación: {self.automatas[i].eAceptacion}')
            print(f'Estado Inicial: {self.automatas[i].eInicial}')
            print(self.automatas[i].path)
            print('Transiciones:')
            for j in range(len(self.automatas[i].transiciones)):
                #print(f'\tOrigen: {self.automatas[i].transiciones[j].origen} Entrada: {self.automatas[i].transiciones[j].entrada} Destino: {self.automatas[i].transiciones[j].destino}')
                print(f'\t{self.automatas[i].transiciones[j].__dict__}')
            print()

    # leyendo archivo

    def reconocimientoAutomata(self):
        self.entrada = self.entrada.split('\n')
        self.identificarElementos()

    def leerArchivo(self,ruta):
        #ruta = 'Automata.afd'
        self.entrada = open(ruta,encoding='utf-8').read()

    def obtenerAlfabeto(self,indice):
        return ', '.join(self.automatas[indice].alfabeto)


#ctrl = ControladorAFD()
#ctrl.leerArchivo()
#ctrl.reconocimientAutomata()
#ctrl.verAutomatas()
#gr = Grafica()
#gr.generarDot(ctrl.automatas[2])