from re import A


def dividir(dividendo, divisor):
    try:
        resultado = round(dividendo / divisor)
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except TypeError:
        print("Has escrito un valor incorrecto para la división. Pon un número.")
    finally:
        print("La operación de división ha finalizado.")
        
        
dividir ("A",1)       