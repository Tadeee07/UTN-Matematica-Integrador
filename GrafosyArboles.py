
# === Árbol de Decisiones Interactivo ===

print("=== Aventura en el Bosque Encantado ===")
inicio = input("¿Deseás comenzar la aventura? (Si/No): ").lower()

if inicio == "si":
    print("\nTe encontrás en un bosque misterioso. Hay dos caminos frente a ti.")
    print("1. Un sendero iluminado por luciérnagas.")
    print("2. Un oscuro túnel entre los árboles.")
    camino = input("¿Qué camino elegís? (1 o 2): ")

    if camino == "1":
        print("\nAvanzás por el sendero iluminado...")
        print("Llegás a un lago brillante con un cofre en el centro.")
        decision = input("¿Querés abrir el cofre? (Si/No): ").lower()

        if decision == "si":
            print("\n¡Dentro del cofre hay un mapa del tesoro! ")
            print("Seguís las indicaciones y encontrás una cabaña mágica llena de oro.")
            print("¡Ganaste la aventura!")
        else:
            print("\nIgnorás el cofre y seguís tu camino.")
            print("De repente, una niebla espesa te rodea y perdés el rumbo...")
            print("Fin del juego.")

    elif camino == "2":
        print("\nEntrás en el túnel oscuro...")
        print("Escuchás un ruido extraño detrás tuyo.")
        accion = input("¿Querés correr o investigar? (Correr/Investigar): ").lower()

        if accion == "correr":
            print("\nCorrés tan rápido como podés y salís del bosque sano y salvo.")
            print("¡Escapaste a tiempo!")
        elif accion == "investigar":
            print("\nTe acercás lentamente... era un lobo hambriento.")
            print("El lobo te ve... y te convertís en su cena.")
            print("Fin del juego.")
        else:
            print("No entendí tu decisión. El bosque te confunde y te perdés.")
            print("Fin del juego.")
    else:
        print("Opción no válida. Te quedás en el mismo lugar para siempre.")
        print("Fin del juego.")
else:
    print("\nFin del programa. Tal vez la próxima vez te animes a jugar. ")