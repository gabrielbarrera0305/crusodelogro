def comparar_numeros(a, b, c):
  mayor = a
  if b > mayor:
    mayor = b
  if c > mayor:
    mayor = c
  menor = a
  if b < menor:
    menor = b
  if c < menor:
    menor = c
  return mayor, menor

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

mayor, menor = comparar_numeros(num1, num2, num3)

print("El número mayor es:", mayor)
print("El número menor es:", menor)