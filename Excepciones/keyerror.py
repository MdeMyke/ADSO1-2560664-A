#este programa llama todos los valores del diccionario
def funcion (dictionary):
    for a in dictionary.values():
        print(a)
    
d={"iphone":"ios",
   "celular":"cell",
   "años":"12"
}
j = input("que informacion quieres ? ")

try:
    print(f"el valor de su solicitud es  {d[j]}")
except KeyError:
    print(f"no hay ningun parametro {j}")
print("los valores almacenados que puedes escoger son ")   

funcion(d)