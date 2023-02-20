def ortografia(c):
    if(c[-1]==chr(225) or c[-1]==chr(233) or c[-1]==chr(237) or c[-1]==chr(243) or c[-1]==chr(250)):
        print('Aguda')
    else:
        print('No es aguda')

ortografia('café')
    


cad="sena"
print(cad)
#cad+=' soacha'
#cap=cad.capitalize()
#print(tam)
lista=list(cad)
#print(lista[2])
print(cad[-1])
print(cad[-2])
print(cad[-3])
print(cad[-4])

palabra = "esdrújula"

if len(palabra) <= 2:
    # Las palabras de una o dos sílabas son siempre agudas
    print("La palabra es aguda")
elif palabra[-1] in "nNsS":
    # Las palabras que terminan en "n", "s" o cualquier letra que no sea una vocal son agudas
    print("La palabra es aguda")
elif palabra[-2:] in ["as", "es", "os"]:
    # Las palabras que terminan en "as", "es", "os" son siempre graves
    print("La palabra es grave")
elif palabra[-3] in "aeiouáéíóú":
    # Si la antepenúltima sílaba es una vocal, la palabra es esdrújula
    print("La palabra es esdrújula")
else:
    # Si la palabra no es aguda, grave ni esdrújula, entonces es sobresdrújula
    print("La palabra es sobresdrújula")
