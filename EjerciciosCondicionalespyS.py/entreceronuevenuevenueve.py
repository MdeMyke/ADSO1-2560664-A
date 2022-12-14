#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene.

print("ingrese un numero entre 0 y 9.999 ")
m = int(input())
if(m<0 or m >9999):
    print("el numero ingresado es invalido")
else:
    if(m<10):
        print("el numero ingresado tiene 1 cifra")
    elif(m<100):
        print("el numero ingresado tiene 2 cifras")
    elif(m<1000):
        print("el numero ingressado tiene 3 cifras")
    elif(m<10000):
        print("el numero ingresado tiene 4 cifras")