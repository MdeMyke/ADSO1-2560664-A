try:#bloquee para ejecutar dar prueba a los errores 
    #print(1/1))
    raise SyntaxError #aqui se a generado el error 
except SyntaxError as e: #se le asigna al syntax error un alias con as 
    print(e) #imprime el alias 
    print('Cierra el parentesis') #imprime la solucion al error 
    
try:#bloquee para ejecutar dar prueba a los errores
    #raise ZeroDivisionError
    print(1/0)#divide por 0 y manda el error 
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde: # se le asigna a ZeroDivisionError un alias con as 
    print(zde)#imprime el alias 
    #print('prueba error')