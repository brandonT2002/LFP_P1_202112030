class GR:
    def __init__(self,nombreGR,noTerminales,terminales,noTerminalInicial,producciones):
        self.nombreGR = nombreGR
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.noTerminalInicial = noTerminalInicial
        self.producciones = producciones

class Produccion:
    def __init__(self,origen,entrada,destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino