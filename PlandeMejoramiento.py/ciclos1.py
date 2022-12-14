'''5.10 Ejercicios
Ejercicio 1: Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de
esos números. Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.'''

cont=0
while True:
  numero = input('Digite un N> ')
  cont+=1
  if numero == 'fin':
   break
       
print(numero)
print('¡Terminado!')
print(cont)







