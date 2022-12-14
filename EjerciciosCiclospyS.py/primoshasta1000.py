# programa para calcular los numeros primos hasta el 10000
numero_primo_hasta = 1000
print("Los números primos hasta el ",numero_primo_hasta)
print("2  es un número primo posición 1") # 2 es el único primo que es par
numero = 3 # se comienza la evaluacion desde 3
cuenta_numero_primos = 1
while numero <= numero_primo_hasta :
    cuenta_divisor_exacto = 1
    for divisor in range(1,round((numero+1)/2)):
        if (numero % divisor) == 0 :
            cuenta_divisor_exacto += 1
    if cuenta_divisor_exacto == 2: # un numero primo tiene 2 divisores exactos
        cuenta_numero_primos += 1
        print(numero," es un número primo posición %d"%cuenta_numero_primos)
    numero += 2 # se consideran los números impares
 
print("Hasta el número %d hay %d números primos"%(numero_primo_hasta,cuenta_numero_primos))
#print("Hasta el número ",numero_primo_hasta," hay ",cuenta_numero_primos," números primos")
