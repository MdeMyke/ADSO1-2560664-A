# Invente un cifrado de texto tipo murcielago o César. 
LONG_LLAVE = 26


def getOpcion():

 while True:
  print ('¿Tu quieres encriptar o desencriptar un mensaje?')
  opcion = raw_input().lower()
  if opcion in 'encriptar e desencriptar d'.split():
   return opcion
  else:
   print ('Escribir "encriptar", "e" o "desencriptar", "d".')


def getMensaje():
 print ('Escribe el mensaje:')
 return raw_input()

def getLlave():
 llave = 0
 while True:
  print('Ingresar la llave (1-%s)' % (LONG_LLAVE))
  llave = int(input())
  if (llave >= 1 and llave <= LONG_LLAVE):
   return llave

def getTraducirMensaje(opcion, mensaje, llave):
 if opcion[0] == 'd':
  llave = -llave
 traducir = ''
 
 for simbolo in mensaje:
  if simbolo.isalpha():
   num = ord(simbolo)
   num += llave

   if simbolo.isupper():
    if num > ord('Z'):
     num -= 26
    elif num < ord('A'):
     num += 26
   elif simbolo.islower():
    if num > ord('z'):
     num -= 26
    elif num < ord('a'):
     num += 26

   traducir += chr(num)
  else:
   traducir += simbolo
 return traducir



opcion = getOpcion()
mensaje = getMensaje()
llave = getLlave()

print('El texto traducido es:')
print(getTraducirMensaje(opcion, mensaje, llave))