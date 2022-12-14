#Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor sin utilizar la división ni el mod.
def main():
    print("DIVISOR DE NÚMEROS")
    j = int(input("Escriba el dividendo-> "))
    u = int(input("Escriba el divisor->"))

    if j % u == 0:
        print(f"La división es exacta. Cociente : {u // j}")
    else:
        print(
            f"La división no es exacta. Cociente: {u // j} "
            f"Resto: {j % u}"
        )


if __name__ == "__main__":
    main()