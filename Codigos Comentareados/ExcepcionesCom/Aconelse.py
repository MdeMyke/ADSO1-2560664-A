try:
    f = open('fichero.txt')  
except FileNotFoundError:
     print('¡El fichero no existe!')
else:
     print(f.read())

