#EJERCICIO 5: 
# ===== NOMBRE =====
nombre = input("Nombre del Gladiador: ")

# valido que solo tenga letras
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# ===== VARIABLES INICIALES =====
vida_jugador = 100      # vida del gladiador
vida_enemigo = 100      # vida del enemigo
pociones = 3            # cantidad de curaciones disponibles

danio_jugador = 15      # daño base del jugador
danio_enemigo = 12      # daño fijo del enemigo

turno_jugador = True    # controlo de quién es el turno


print("\n=== INICIO DEL COMBATE ===")


# ===== CICLO PRINCIPAL =====
# se repite mientras ambos tengan vida
while vida_jugador > 0 and vida_enemigo > 0:

    # ===== TURNO DEL JUGADOR =====
    if turno_jugador:

        # muestro el estado actual
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

        # menú de acciones
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        # validación de número
        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        # validación de rango
        while opcion != "1" and opcion != "2" and opcion != "3":
            print("Error: Opción inválida.")
            opcion = input("Opción: ")


        # =========================
        # ACCIÓN 1: ATAQUE PESADO
        # =========================
        if opcion == "1":

            # daño base
            danio_final = danio_jugador

            # si el enemigo está débil (<20 HP), se activa crítico
            if vida_enemigo < 20:
                danio_final = danio_jugador * 1.5  

            # aplico el daño
            vida_enemigo -= danio_final

            # muestro resultado
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

            # esta acción hace mucho daño de una sola vez


        # =========================
        # ACCIÓN 2: RÁFAGA VELOZ
        # =========================
        elif opcion == "2":

            print(">> ¡Inicias una ráfaga de golpes!")

            # se ejecuta 3 veces usando for
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

            # esta acción hace daño en partes (3 golpes pequeños)


        # =========================
        # ACCIÓN 3: CURAR
        # =========================
        elif opcion == "3":

            # si hay pociones disponibles
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te curaste 30 puntos de vida.")

            else:
                print("¡No quedan pociones!")

            # esta acción recupera vida pero consume recurso


        # termina turno del jugador
        turno_jugador = False


    # ===== TURNO DEL ENEMIGO =====
    else:

        # el enemigo siempre ataca automáticamente
        vida_jugador -= danio_enemigo

        print(f">> ¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

        # vuelve el turno al jugador
        turno_jugador = True


# ===== FIN DEL JUEGO =====

# si el jugador sigue vivo → gana
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")

# si no → pierde
else:
    print("DERROTA. Has caído en combate.")
    