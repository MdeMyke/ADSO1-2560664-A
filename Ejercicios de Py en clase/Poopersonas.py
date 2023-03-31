class Persona:#se crea una clase llamada persona 
    def __init__(self,nombre,documento):#se crea el constructor el cual es un metodo y por eso se mete en una funcion  
        self.__nombre=nombre#self significa que es de aqui que aclara que esta en la clase persona 
        self.__documento=documento  #las dos lineas bajas son para poner en privado documento       
    def getdocumento(self):#metodo para retornar en este caso el documento dado
        return self.__documento

    def setdocumento(self,documento):#modificar el metodoto y valor 
        self.__documento=documento

    def getNombre(self):#retornar en este caso el nombre dado 
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

        
ob=Persona('Maria')#instancia la clase persona = objeto 
print(ob.getNombre())#imprime los valores atribuidos a getnombre 
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):#se crea una subclase dentro de aprendiz 
    def __init__(self,nombre,documento,ficha):
        Persona.__init__(self,nombre,documento)#se eredan los valores de personas 
        self.__ficha=ficha
        
    def getFicha(self):#metodo para retornar el valor de ficha  
        return self.__ficha
    
app=Aprendiz('Pedro',1000627628,2560664)#objeto de aprendiz donde se ubican los valores 
print(app.getFicha())#imprime lo retornado en getficha
print(app.getNombre())#imprime lo retornado en getnombre 
print(app.getdocumento())#imprime lo retornado en getdocumento