'''Ejercicio
Dada una cadena de texto, indique el número de vocales que tiene.'''

def ov(frase):
    vocales = input('ingrese una frase: ')

    return set([c for c in frase if c in vocales])

texto = 'Python es genial'

print(ov(texto))
print(len(ov(texto)))