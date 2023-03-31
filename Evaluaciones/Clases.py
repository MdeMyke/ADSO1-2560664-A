class pedido:
    def __init__(self,idusuario,titulomat,codigomat):
        self.__idusuario=idusuario
        self.titulomat=titulomat
        self.__codigomat=codigomat
        self.__fechaini=[]
        self.__fechafin=[]
    def agregarreserva(self,fechaini,fechafin):
        self.__fechaini.append(fechaini)
        self.__fechafin.append(fechafin)
    def verreservaini(self):
        return self.__fechaini
    def verreservafin(self):
        return self.__fechafin
        
        
    def getidusuario(self):
        return self.__idusuario

    def setidusuario(self,idusuario):
        self.__idusuario=idusuario

    def gettitulomat(self):
        return self.titulomat

    def settitulomat(self,titulomat):
        self.titulomat=titulomat
    
    def getcodigomat(self):
        return self.__codigomat

    def setcodigomat(self,codigomat):
        self.__codigomat=codigomat
    
    
    
class reserva:
    
    def __init__(self,fechaini,fechafin):
        self.fechaini=fechaini
        self.fechafin=fechafin

    def getfechaini(self):
        return self.fechaini
    def getfechafin(self):
        return self.fechafin
    
ob1=pedido(53078549,"Pepitoysucuentico",984564)
c1=reserva('6/3/2023',())
c2=reserva('8/4/2023',())
ob1.agregarreserva(c1,c2)

print(ob1.getidusuario())
print(ob1.gettitulomat())
print(ob1.getcodigomat())

for Reserva in ob1.verreservaini():
    print(Reserva.getfechaini())
    
for Reservaa in ob1.verreservafin():
    print(Reservaa.getfechafin())


del ob1

print(c1.getfechaini())



class material:
    def __init__(self,autor,editorial):
     self.autor=autor
     self.editorial=editorial

    def getautor(self):
        return self.autor

    def setautor(self,autor):
        self.autor=autor

    def geteditorial(self):
        return self.editorial

    def seteditorial(self,editorial):
        self.editorial=editorial

class libro(material,reserva):
    def __init__(self,autor,editorial,fechaini,fechafin,titlibro,tiplibro):
        material.__init__(self,autor,editorial)
        pedido.__init__(self,fechaini,fechafin)
        self.__titlibro=titlibro
        self.tiplibro=tiplibro

    def gettitlibro(self):
        return self.__titlibro
    
    def gettiplibro(self):
        return self.s






            

            


        