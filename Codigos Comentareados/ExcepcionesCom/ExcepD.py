def edad(): #se crea una funcion edad 
    try:
        tuedad=int(input("introduce tu edad"))# variable tuedad en ella se int input para que se ingrese y solo sean admitidos numeros 
        print(f'tu edad es  {tuedad}')# imprime la edad y la f es para que se pueda colocar la variable dentro de las comillas 
        #print('Tu edad es ',tuedad)
    except ValueError as e: # se le asigna a valueerror el alias e 
        print(e)# imprime el error 
        print("La edad debe ser un valor numerico...")#indica la solucion 
        edad()#muestra la edad 
    
edad()