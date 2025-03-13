def juego():
    print("¡Bienvenido a la Aventura!")
    print("Eres un valiente aventurero que comienza su viaje.")
    print("Te encuentras en un cruce de caminos.")

    while True:
        print("\n¿Qué camino tomarás?")
        print("1. Ir hacia el BOSQUE OSCURO<-")
        print("2. Ir hacia la ALDEA->")
        decision= input("Elige una opción (BOSQUE OSCURO o ALDEA): ").upper()

        if decision== "BOSQUE OSCURO":
            bosque_oscuro()
            break
        elif decision== "ALDEA":
            aldea()
            break
        else:
            print("¡Opción no válida! Intenta de nuevo.")

def bosque_oscuro():
    print("\nTe adentras en el BOSQUE OSCURO...")
    print("El aire es frío y los árboles susurran misteriosamente.")
    print("De repente, encuentras un cofre antiguo y un camino que lleva más adentro del bosque.")

    while True:
        print("\n¿Qué harás?")
        print("1. ABRIR el cofre<-")
        print("2. SEGUIR el camino->")
        decision= input("Elige una opción (ABRIR o SEGUIR): ").upper()

        if decision== "ABRIR":
            print("\nAbres el cofre y encuentras un mapa del tesoro. ¡Felicidades!")
            print("Has logrado una famosa legenda, que se recordara por muchos años. ¡Juego terminado!")
            print("Gracias por jugar")
            break
        elif decision== "SEGUIR":
            print("\nSigues el camino y te pierdes en el bosque para siempre...")
            print("¡Fin del juego! :C")
            break
        else:
            print("¡Opción no válida! Intenta de nuevo.")

def aldea():
    print("\nLlegas a la ALDEA...")
    print("Los aldeanos te reciben con alegría y te ofrecen ayudarte.")
    print("Puedes quedarte en la aldea y vivir traquilo o buscar más aventuras y ser recordado como un legendario herue.")

    while True:
        print("\n¿Qué harás?")
        print("1. QUEDARSE en la aldea<-")
        print("2. BUSCAR más aventuras->")
        decision= input("Elige una opción (QUEDARSE o BUSCAR): ").upper()

        if decision== "QUEDARSE": 
            print("\nTe quedas en la aldea y vives una vida tranquila.")
            print("¡Fin del juego! :D")
            print("Gracias por jugar")
            break
        elif decision== "BUSCAR":
            print("\nDecides buscar más aventuras y te conviertes en un héroe legendario.")
            print("Has logrado ser una legenda que se contara por mucho años. ¡Juego terminado!")
            print("Gracias por jugar :D")
            break
        else:
            print("¡Opción no válida! Intenta de nuevo.")

juego()