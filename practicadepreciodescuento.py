precio = int(input("Ingresar el precio"))
descuento = int(input("Ingresar el porcentaje de descuento"))
precio_total = precio - ((precio * descuento) / 100)

print("el precio con descuento es: " + str(precio_total))

if precio_total < 100:
    print ("el precio con descuento es menor a 100")
else: 
    print ("el precio con descuento es mayor a 100")