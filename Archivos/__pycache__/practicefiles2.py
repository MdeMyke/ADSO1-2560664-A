from Aprendiz import *#importa los metodos  y demas de las clases curso y aprendiz
from Curso import *

 nombre=input('ingrese nombre del aprendiz')#------->
 documento=int(input('ingrese documento del aprendiz'))#-------> ingresar los parametros que se van a instanciar por teclado 
 ficha=input('ingrese ficha del aprendiz')#------->

 ap=Aprendiz(ficha,nombre,documento)# agrga e instancia la clase con sus debidos parametros 

 nombreCurso=input('ingrese nombre del curso')
 horas=int(input('ingrese intensidad horaria del curso'))
 c1=Curso(nombreCurso,horas)
 ap.agregarCurso(c1)#ap=append para agregar cursos, esta agregando cursos a c1 

 with open('herencia/aprendices.txt','a') as flujo:    
     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')#concatena los diferentes get a imprimir o retonar, no olvidar que documento debe ser tipo str para que se sea valido ademas de que /n es para hacer salto de linea 



with open('herencia/aprendices.txt','r') as flujo:
    datos=flujo.read()    
    print(datos)
    #flujo.write('2560664,maria,123')
aprendices=[]
with open('herencia/aprendices.txt','r') as flujo:
    for linea in flujo:
        #print(linea)
        aprendices.append(linea.rsplit())#rsplit para hace que los parametros queden en una lista de dentro de una lista 

datosxlinea=[]#crea una lista 
for aprendiz in aprendices:# este pasara por cada uno de los elementos de la lista aprendices 
    datosxlinea.append(aprendiz[0].split(','))#en esta lista agregara el elemento que este en la posicion 0 de la lista, el split indica la division de los elementos separados por , 



#print(ob.getNombre())

print(datosxlinea)# impime la lista 

listaDeObjetos=[]# se crea otra lista 
for apr in datosxlinea:#van a recorrer la lista 
     f=apr[0]#variable que almacena el elemento 0 de la lista 
     n=apr[1]#variable que almacena el elemento 1 de la lista 
     d=apr[2]#variable que almacena el elemento 2 de la lista 
     ob=Aprendiz(f,n,d)#se crea un objeto de la clase aprendiz con las variables anteriores 
     print(ob)# la imprime 
     listaDeObjetos.append(ob)# agreaga a la lista el objeto 


for xx in listaDeObjetos:#recorre la lista 
    print(xx.getNombre())
    print(xx.getDocumento())#-------> imprime cada elemento por aparte 
    print(xx.getFicha())