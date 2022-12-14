#Calcular la operación x n sin utilizar la función pow
def potencia(j, n):
    u = 1  
    a = 1 
    while u <= n:
        a = a * j
        u = u + 1
    return a
print(potencia(2, 3))  
print(potencia(2, 4))  
print(potencia(2, 5))  
print(potencia(2, 0))  
print(potencia(2, 1))  
print(potencia(11, 3))  
print(potencia(2, 31))  
print(potencia(5, 2))  