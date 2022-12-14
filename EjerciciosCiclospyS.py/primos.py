#DETERMINAR SI UN NUMERO ES PRIMO O NO PRIMO:
n =int(input("ingresa un numero> "))
l = 1
j = 0
while l <=n:
    if n % l == 0:
        j = j + 1  
    X = X + 1    
if j == 2:
    print("el numero ",n,"es primo")
else:
    print("el numero ",n,"no es primo")            


