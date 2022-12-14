"""Escribe un programa que pida tres números y que escriba si son los tres 
iguales, si hay dos iguales o si son los tres distintos"""

num1 = int(input("digite el primer num"))
num2 = int(input("digite el segundo num"))
num3 = int(input("digite el tercer num"))

if num1==num2==num3:
    print ('Los tres numeros son iguales')
elif num1==num2 or num1==num3 or num2==num3:
    print ('Hay dos numeros iguales')
else:
    print ('Los tres numeros son distintos')