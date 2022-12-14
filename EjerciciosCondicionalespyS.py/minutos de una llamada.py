#Ingrese los minutos que duró la llamada

banderazo = 200
m = int(input('Ingrese los minutos que duró la llamada'))
if m <= 3:
    print('La llamada de fue de',m, 'minutos, por lo cual el pago será de',banderazo)
else:
    me = m-3
    total = (me*50) + banderazo
    print('La llamada de fue de',m, 'minutos, por lo cual el pago será de',total)