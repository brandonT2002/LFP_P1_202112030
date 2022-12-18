class GR:
    def __init__(self):
        self.nombreGR = None
        self.noTerminales = None
        self.eAceptacion = None
        self.terminales = None
        self.noTerminalInicial = None
        self.producciones = None
        self.path = {}

class Produccion:
    def __init__(self,origen,entrada,destino = 'ACEPTADO'):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino