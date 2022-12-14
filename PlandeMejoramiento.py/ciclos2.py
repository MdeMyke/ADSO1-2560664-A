"""Ejercicio 2: Escribe otro programa que pida una lista de números como
la anterior y al final muestre por pantalla el máximo y mínimo de los
números, en vez de la media."""



while True:
  numero = input('Digite un N> ')

  if numero == 'fin':
   break
mayor = None
print('Antes:', mayor)
for valor in [numero]:
  if mayor is None or valor > mayor :
   mayor = valor

   
print('Bucle:', valor, mayor)
print('Mayor:', mayor)
print(numero)
print('¡Terminado!')

