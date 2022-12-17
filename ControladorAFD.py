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

    def agregarAFD(self,nombre,estados,alfabeto,eInicial,eAcept,transiciones,diccionario):
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

        automata.transiciones = trans
        automata.path = diccionario

        self.automatas.append(automata)

    def cadenaMinima(self,cadenas,diccionario,estado,acept,alf,cadena,cont) -> list:
        if cont > 20:
            return
        if estado in acept:
            cadenas.append(cadena)
            return
        destinos = diccionario[estado]
        if len(cadenas) > 30:
            return
        for entrada in alf:
            try:
                self.cadenaMinima(cadenas,diccionario,destinos[entrada],acept,alf,cadena + entrada,cont + 1)
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