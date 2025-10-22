
#2. CALCULADORA

from operaciones import suma, resta, multiplicacion, division

def menu():
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedirNumero1():
    while True:
        try:
            return float(input("Introduce primer número: "))
        except ValueError:
            print("Error: debes escribir un número válido.")

def pedirNumero2():
    while True:
        try:
            return float(input("Introduce segundo número: "))
        except ValueError:
            print("Error: debes escribir un número válido.")


def calculadora():
    while True:
        menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("=== FIN ===")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida.")
            print("")
            continue

        num1 = pedirNumero1()
        num2 = pedirNumero2()

        if opcion == "1":
            resultado = suma(num1, num2)
        elif opcion == "2":
            resultado = resta(num1, num2)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
        elif opcion == "4":
            resultado = division(num1, num2)


        print(f"Resultado: {resultado}")
        print("")

# Así solo ejecuta el programa si este archivo se ejecuta directamente.
if __name__ == "__main__":
    calculadora()
