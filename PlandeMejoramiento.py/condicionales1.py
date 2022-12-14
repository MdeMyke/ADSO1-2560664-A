"""Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es.
 Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre
100, o bien si es divisible entre 400."""

a=int(input("digite un año: "))

if a /4:
    if a /400:
     print("es un año biciesto")
else :
    print('no es biciesto: ')
