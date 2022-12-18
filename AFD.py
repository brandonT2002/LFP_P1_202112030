class AFD:
    def __init__(self):
        self.nombreAFD = None
        self.estados = None
        self.alfabeto = None
        self.eInicial = None
        self.eAceptacion = None
        self.transiciones = None
        self.path = {}

class Transicion:
    def __init__(self,origen,entrada,destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino