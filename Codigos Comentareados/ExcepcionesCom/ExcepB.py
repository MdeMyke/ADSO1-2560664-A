values = (1, 0) #una tupla que divide 
#x,y=10,12
#print(divmod(10,3))
try:
    q, r = divmod(*values) # q y r son los dividendos = divmod es para dividir, values para coger 
    #los elementos de la tupla y el asterisco para separar cada uno de los elementos
    #print('valor de q=',q)
    print(f'q={q}')# la f sirve para que la variable se pueda poner dentro de las comillas e imprimir la variable 
    print(f'r={r}')# la f sirve para que la variable se pueda poner dentro de las comillas e imprimir la variable 
except (ZeroDivisionError, TypeError) as e:# es para para que las dos excepciones queden asignadas en el alias e
    print(type(e), e)# ya con type revisa cual de las dos except es y lo imprime 
