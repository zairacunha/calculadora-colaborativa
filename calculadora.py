# calculadora.py - Calculadora Colaborativa
def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n=== Calculadora Colaborativa ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ")
        
        if opcion == '0':
            print("¡Hasta luego!")
            break
        elif opcion == '1':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a} + {b} = {sumar(a, b)}")

        elif opcion == '2':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a} - {b} = {restar(a, b)}")
        
        elif opcion == '3':
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {a} * {b} = {multiplicar(a, b)}")
            
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    main()