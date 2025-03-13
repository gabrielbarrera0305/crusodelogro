estudiantes= int(input("Ingrese el numero de estudiantes: "))

calif= []

for i in range(estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
    calif.append(calificacion)

suma_calif= sum(calif)

promedio= suma_calif / estudiantes

calif_maxima= max(calif)
calif_minimo= min(calif)

print(f"\nSuma de las calificaciones: {suma_calif}")
print(" ")
print(f"Promedio de las calificaciones: {promedio}")
print(" ")
print(f"Calificación más alta: {calif_maxima}")
print(f"Calificación más baja: {calif_minimo}")