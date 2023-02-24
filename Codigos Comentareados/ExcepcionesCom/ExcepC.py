def try_syntax(numerator, denominator): # se crea funcion con dos parametros 
    try:
        result = numerator / denominator #se crea la variable result para la operacion echa 
        print(f'In the try block: {numerator}/{denominator}/El resultado es: {result}') #imprime los argumentos ingresados 
    
        
       
    except ZeroDivisionError as zde: # se le asigna a ZeroDivisionError un alias con as
        print(zde) #imprime el alias 
    else:
        print('The result is:', result)# imprime el resultado 
        return result #termina la ejecucion de la funcion llamada 
    finally:
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 4)) 