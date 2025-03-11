num1= int(input("ingrese numero 1:"))
num2= int(input("ingrese numero 2:"))
resul= num1 and num2 >= 0
resul2= num1 and num2 < 0
resul3= num1 < 0
print (f"ambos numeros son positivos:{resul}")
print (f"al menos un numero es negativo:{resul2}")
print (f"el primer numero es negativo:{resul3}")