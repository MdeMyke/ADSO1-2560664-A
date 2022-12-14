"""Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el 
valor del medio es 11. No use operadores lógicos"""

num1 = int(input("digite el primer num"))
num2 = int(input("digite el segundo num"))
num3 = int(input("digite el tercer num"))

menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
medio = (num1 + num2 + num3) - menor - mayor 

print("El numero de enmedio es:", medio)
