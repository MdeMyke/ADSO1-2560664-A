flujo=open('Archivos/inicio.txt','r')#open es un metodo para abrir un archvio escogido se debe poner la ruta en la cual se encuentra y si no esta 
#se pone el nombre deseado par a el nuevo archivo ene este caso inicio.txt y el lo creara pa ejecutar el comando y ,a es para adjuntar 
#datos=flujo.read() 
#print(datos)
flujo.write('\nCuando estudian con juicio')# write es otro metodo el cual es para leer, el codigo lo leera y pondra lo leido en el archivo indicado 
datos=flujo.read()#ya read es el metodo para  escribir 
print(datos)#imprime el codigo 
