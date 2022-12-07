class AFD:
    def __init__(self,nombreAFD,estados,alfabeto,eInicial,eAceptacion,transiciones):
        self.nombreAFD = nombreAFD
        self.estados = estados
        self.alfabeto = alfabeto
        self.eInicial = eInicial
        self.eAceptacion = eAceptacion
        self.transiciones = transiciones

class Transicion:
    def __init__(self,origen,entrada,destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino