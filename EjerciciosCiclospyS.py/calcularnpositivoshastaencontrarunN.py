"""Calcular el máximo de números positivos introducidos por 
teclado, sabiendo que metemos números hasta que 
introduzcamos uno negativo. El negativo no cuenta"""
suma = 0 
cantidad = 0 
num = 0
while(num >=0):
    num = int(input("digite un nun o un num- para salir"))
    suma = suma + num
    cantidad = cantidad+1
 
print ("suma: ",suma,)
print ("cantidad: ",cantidad)