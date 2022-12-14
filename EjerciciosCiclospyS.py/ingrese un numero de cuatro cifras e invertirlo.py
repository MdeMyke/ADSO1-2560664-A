#ingrese un numero de cuatro cifras e invertirlo#

A = int (input( "ingrese un numero de nueve cifras" ))
c9 = A % 10 
c8 = int ((A % 100)/10)
c7 = int ((A % 1000)/100)
c6 = int ((A % 10000)/1000)
c5 = int ((A % 100000)/10000)
c4 = int ((A % 1000000)/100000)
c3 = int ((A % 10000000)/1000000)
c2 = int ((A % 100000000)/10000000)
c1 = int (((A % 1000000000)) / 100000000)
print(str(c9)+str(c8)+str(c7)+str(c6)+str(c5)+str(c4)+str(c3)+str(c2)+str(c1))
