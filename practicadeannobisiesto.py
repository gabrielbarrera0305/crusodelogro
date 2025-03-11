anno= int(input("Ingresar el año"))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print ("el año es bisiesto")
else: 
    print ("el año no es bisiesto")