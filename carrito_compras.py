def agregar_producto(carrito):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append((producto, precio))
    print(f"'{producto}' ha sido agregado al carrito.\n")
    return carrito

def mostrar_carrito(carrito):
    if not carrito:
        print("El carrito está vacío.\n")
    else:
        print("Contenido del carrito:")
        for i, (producto, precio) in enumerate(carrito, start=1):
            print(f"{i}. {producto} - ${precio:.2f}")
            print()

def eliminar_producto(carrito):
    mostrar_carrito(carrito)
    if carrito:
        try:
            indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
            if 0 <= indice < len(carrito):
                producto_eliminado = carrito.pop(indice)
                print(f"'{producto_eliminado[0]}' ha sido eliminado del carrito.\n")
            else:
                print("Número de producto inválido.\n")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.\n")
    else:
        print("No hay productos para eliminar.\n")
    return carrito

def calcular_total(carrito):
    total = sum(precio for _, precio in carrito)
    print(f"El total de la compra es: ${total:.2f}\n")

def main():
    carrito = []  # Definir carrito como una variable local en main
    while True:
        print("Bienvenido a Mama Flor, elige los productos que quieras:")
        print("1. Agregar producto")
        print("2. Mostrar contenido del carrito")
        print("3. Eliminar producto")
        print("4. Calcular total")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            carrito = agregar_producto(carrito)  # Actualizar carrito
        elif opcion == "2":
            mostrar_carrito(carrito)
        elif opcion == "3":
            carrito = eliminar_producto(carrito)  # Actualizar carrito
        elif opcion == "4":
            calcular_total(carrito)
        elif opcion == "5":
            print("Gracias por visitar Mama Flor. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()
