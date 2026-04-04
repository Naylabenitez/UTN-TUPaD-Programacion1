#Ejercicio 4:
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

# ===== NOMBRE =====
nombre = input("Ingresá tu nombre: ")
while not nombre.isalpha():
    nombre = input("Nombre inválido: ")

# ===== JUEGO =====
while True:

    # condiciones de salida
    if cerraduras_abiertas == 3:
        print("VICTORIA")
        break

    if energia <= 0 or tiempo <= 0:
        print("DERROTA")
        break

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("DERROTA POR BLOQUEO")
        break

    # ===== ESTADO =====
    print("\n--- ESTADO ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")

    # ===== MENÚ =====
    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        opcion = input("Opción inválida: ")

    while opcion != "1" and opcion != "2" and opcion != "3":
        opcion = input("Fuera de rango: ")

    # ===== OPCIÓN 1 =====
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            print("Se trabó la cerradura. ALARMA.")
            alarma = True
            continue

        if energia < 40:
            numero = input("Elegí número (1-3): ")

            while not numero.isdigit():
                numero = input("Número inválido: ")

            while numero != "1" and numero != "2" and numero != "3":
                numero = input("Fuera de rango: ")

            if numero == "3":
                alarma = True

        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")

    # ===== OPCIÓN 2 =====
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for i in range(4):
            print(f"Hackeando paso {i+1}")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hack completo.")

    # ===== OPCIÓN 3 =====
    elif opcion == "3":
        tiempo -= 1
        energia += 15

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

        racha_forzar = 0

    
