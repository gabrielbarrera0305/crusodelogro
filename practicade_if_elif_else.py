num= int(input("ingrese la temperatura del agua:"))
if num >= 90 and 100:
    print ("el agua esta hirviendo")
elif num >= 80 and 89:
    print ("falta 5 minutos para hervir")
elif num >= 70 and 79:
    print ("falta 10 minutos para hervir")
elif num >= 60 and 69:
    print ("falta 15 minutos para hervir")
elif num >= 0 and 59:
    print ("falta de 35 a 20 minutos o esta muy fia")
else:
    print ("es hielo :b")