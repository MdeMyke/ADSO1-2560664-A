#multiplos de 5

def u(j, u):
    return True if j % u == 0 else False
multiples_5=[]
for i in range(1, 101):
    if u(i, 5):
        multiples_5.append(i)
print ("\nLos multiples de 5 son->", multiples_5)