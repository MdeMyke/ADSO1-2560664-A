'''Usando un diccionario, cuente el número de veces que se repite cada letra en una cadena de
texto dada.'''

sentence = input('ingrese una cadena de texto: ')
pepito = {}

for letter in sentence:
    if letter in pepito:
        pepito[letter] += 1
    else:
        pepito[letter] = 1

print(pepito)
