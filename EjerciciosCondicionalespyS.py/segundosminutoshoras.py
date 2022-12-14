"""Solicite al usuario una cantidad numérica que expresa segundos (medida de 
tiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso"""

m=input("ingrese cantidad de segundos:")
m=int(m)
horas=m//3600
sobrante1=m%3600
minutos=sobrante1//60
sobrante2=sobrante1%60
print("horas")
print(horas)
print("minutos")
print(minutos)
print("segundos")
print(sobrante2)