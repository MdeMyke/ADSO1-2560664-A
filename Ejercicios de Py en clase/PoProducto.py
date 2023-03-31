class producto:
    def __init__(self,nombre,precio,iva):
        self.__nombre=nombre
        self.__precio=precio
        self.__iva=iva
    def getnombre(self):
        return self.__nombre

    def setnombre(self,nombre): 
        self.__nombre=nombre

    def getprecio(self): 
        return self.__precio

    def setprecio(self,precio):
        self.__precio=precio

    def getiva(self):
        return self.__iva

    def getcalcular(self):
        return self. getprecio + getiva()

    
        

 
      

            
pr1=producto('televisor',900000,19/100)
print(pr1.getnombre())
print(pr1.getprecio())
print(pr1.calculariva())
pr2=producto('computador',800000,19)
print(pr2.getnombre())
print(pr2.getprecio())
    


