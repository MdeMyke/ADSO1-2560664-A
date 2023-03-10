class Persona:#se crea la clase persona con sus debidos get y seters 
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setDocumento(self,documento):
        self.__documento=documento