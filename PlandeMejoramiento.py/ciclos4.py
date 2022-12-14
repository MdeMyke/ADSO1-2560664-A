'''Determine si un número dado es un número primo.
No es necesario implementar ningún algoritmo en concreto. La idea es probar los números
menores al dado e ir viendo si las divisiones tienen resto cero o no.
¿Podría optimizar su código? ¿Realmente es necesario probar con tantos divisores?'''

def main():
    print("NÚMERO PRIMO")
    numero = int(input("Escriba un número entero mayor que 1: "))

    if numero <= 1:
        print("¡Le he pedido un número entero mayor que 1!")
    else:
        contador = 0
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 2:
            print(f"{numero} es primo.")
        else:
            print(f"{numero} no es primo.")


if __name__ == "__main__":
    main()

