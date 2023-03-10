from Persona import * # se importa la clase persona 
#from Curso import * ...en caso de composición
class Aprendiz(Persona):#se crea la clase aprendiz y se hereda persona 
    def __init__(self,ficha,nombre,documento):# se crea el constructot con los parametros de las dos clases 
        Persona.__init__(self,nombre,documento)#se crea el constructor de la clase persona 
        self.__ficha=ficha
        self.__cursos=[]
    def getFicha(self):
        return self.__ficha
    def setNombre(self,ficha):
        self.__ficha=ficha
    def agregarCurso(self,curso):#---->para poder agregar los cursos se crea el metodo y se le agrega append 
        #c=Curso('python',120) 
        self.__cursos.append(curso)
    def getCursos(self):
        return self.__cursos