# Función para agregar compra a la lista
def agregar_compra(compras, total_gastado):
    monto = float(input("Ingresa el monto de la compra: $"))
    compras.append(monto)
    total_gastado += monto
    print(f"Compra de ${monto} agregada correctamente.")
    return total_gastado

# Función para mostrar las compras
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras registradas:")
        for i, compra in enumerate(compras, 1):
            print(f"*Compra {i}: ${compra}")

# Función para mostrar el total gastado
def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")

# Función principal del programa
def main():
    compras = []
    total_gastado = 0

    while True:
        print("="* 50)
        print("\nMenú de Compras:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        print("=" * 50)

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida (1-4).")

main()