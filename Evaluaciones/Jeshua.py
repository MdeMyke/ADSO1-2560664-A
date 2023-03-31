class usuario:
    def __init__(self,nombre,direccion,telefono,cuenta):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__cuenta=cuenta
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    def getcuenta(self):
        return self.__cuenta
    def getcont(self):
        if self.__cuenta=="#":
            print("Ingreso con usuario de estudiante")
        elif self.__cuenta=="@":
            print("Ingreso con usuario de docente")
        else:
            print("tipo de usuario no encontrado")

class material(usuario):
    def __init__(self,titulo,tipo,autor,editorial):
        self.__titulo=titulo
        self.__tipo=tipo
        self.__autor=autor
        self.__editorial=editorial

    
    def settitulo(self,titulo):
        self.__titulo=titulo
    def gettitulo(self):
        return self.__titulo
    def settipo(self,tipo):
        self.__tipo=tipo
    def gettipo(self):
        return self.__tipo
    def setautor(self,autor):
        self.__autor=autor
    def getautor(self):
        return self.__autor
    def seteditorial(self,editorial):
        self.__editorial=editorial
    def geteditorial(self):
        return  self.__editorial
            
ob1=material('Satanas','suspenso','mario mendoza','casalibro')
ob2=material('Escorpion City','suspenso','mario mendoza','casalibro')

ob3=material
ob4=material()

ob1.settitulo('satanas')
ob1.settipo('suspenso')
ob1.setautor('mario mendoza')
ob1.seteditorial('casalibro')
ob2.settitulo('Escorpion City')
ob2.settipo('suspenso')
ob2.setautor('mario mendoza')
ob2.seteditorial('casalibro')

print(ob1.gettitulo())
print(ob1.gettipo())
print(ob1.getautor())
print(ob1.geteditorial())
print(ob2.gettitulo())
print(ob2.gettipo())
print(ob2.getautor())
print(ob2.geteditorial())


        

#///////////////////////////////////////////////////////////////////////////////
class pedido(material):
    def __init__(self,dato,id,titulo,codigo):
        self.__id=id
        self.__titulo=titulo
        self.__codigo=codigo
        material .__init__(self,dato)
    def getid(self):
        return self.__id
    def gettitulo(self):
        return self.__titulo
    def getcodigo(self):
        return self.__codigo
    def getpedido(self):
        print("Datos del pedido:")
        print("Id:",z.getid())
        print("Titulo:",z.gettitulo())
        print("Codigo",z.getcodigo())
        print("----------------------")
        print("Datos del material:")
        print(z.getdat())
class bibliotecario(usuario):
    def __init__(self,nombre,direccion,telefono,cuenta,idb):
        self.__idb=idb
        usuario .__init__(self,nombre,direccion,telefono,cuenta)
    def getbibli(self):
        return self.__idb
    def getd(self):
        print("---------------------")
        print("Datos de usuario")
        print("Nombre:",a.getnombre())
        print("Dirección:",a.getdireccion())
        print("Telefono:",a.gettelefono())
        print(a.getcont())
        print("---------------------")
        print("Datos del biliotecario")
        print("ID:",a.getbibli())
        print("---------------------")
c=input("Ingrese # si es estudiante//Ingrese @ si es docente:")
a=bibliotecario("Luis","Kr-15",213828,c,6362363)
a.getd()
x=input("Ingrese 1 para los datos del libro//Ingrese 2 para los datos de la revista:")
z=pedido(x,112312,"Scorpio city",62363)
z.getpedido()