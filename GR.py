class GR:
    def __init__(self):
        self.nombreGR = None
        self.noTerminales = None
        self.terminales = None
        self.noTerminalInicial = None
        self.producciones = None

class Produccion:
    def __init__(self,origen,entrada,destino = ''):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino