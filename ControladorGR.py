from GR import *

class ControladorGR:
    def __init__(self):
        self.gramaticas = []
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
            self.gramatica = GR()
            self.gramatica.nombreGR = self.sacarLinea()
        elif self.linea == 1:
            self.gramatica.noTerminales = self.sacarLinea().split(',')
        elif self.linea == 2:
            self.gramatica.terminales == self.sacarLinea().split(',')
        elif self.linea == 3:
            self.gramatica.noTerminalInicial == self.sacarLinea()
        elif self.linea == 4:
            self.producciones = []
        if self.linea >= 5:
            produccion = self.sacarLinea().split('>')
            destinoEntrada = produccion[1].replace(' ','')
            if destinoEntrada != '$':
                self.producciones.append(Produccion(produccion[0].replace(' ',''),destinoEntrada[0],destinoEntrada[1]))
            else:
                self.producciones.append(Produccion(produccion[0].replace(' ',''),destinoEntrada))
        self.linea += 1
        if self.verLinea() == '%' or not self.verLinea():
            self.gramatica.producciones = self.producciones
            self.gramaticas.append(self.gramatica)
            self.sacarLinea()
            self.linea = 0
        if self.verLinea():
            self.identificarElementos()

    def agregarGramatica(self,nombre,noTerminales,terminales,noTermIni,producciones):
        prod = []
        gramatica = GR()
        gramatica.nombreGR = nombre
        gramatica.noTerminales = noTerminales.split(';')
        gramatica.terminales = terminales.split(';')
        gramatica.noTerminalInicial = noTermIni
        
        for i in producciones:
            valor = i.split(' ')
            prod.append(Produccion(producciones[0],valor[0],valor[1]))

        gramatica.producciones = prod

        self.gramaticas.append(gramatica)

    def verGramaticas(self):
        for i in range(len(self.gramaticas)):
            print(f'Nombre: {self.gramaticas[i].nombreGR}')
            print(f'No terminales: {self.gramaticas[i].noTerminales}')
            print(f'Terminales: {self.gramaticas[i].terminales}')
            print(f'No terminal inicial: {self.gramaticas[i].noTerminalInicial}')
            print(f'Producciones: ')
            for j in range(len(self.gramaticas[i].producciones)):
                print(f'\t{self.gramaticas[i].producciones[j].__dict__}')
            print()

    def reconocimientoGramatica(self):
        self.entrada = self.entrada.split('\n')
        self.identificarElementos()

    def leerArchivo(self,ruta):
        #ruta = 'Gramatica.grm'
        self.entrada = open(ruta,encoding='utf-8').read()

#ctrl = ControladorGR()
#ctrl.leerArchivo()
#ctrl.reconocimientoGramatica()
#ctrl.verGramaticas()