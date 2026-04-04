#Ejercicio 3: 

#Primero, defino las variables con vacíos: 
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Operador nombre: 
operador = input("Ingresá tu nombre de operador: ")

while not operador.isalpha():
    operador = input("Nombre inválido. Ingresá nuevamente: ")

# MENÚ PRINCIPAL
while True:
    print("\nBienvenido al menú")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Selecciona una opción ")

    #Si la opción no es número:
    if not opcion.isdigit():
        print("ERROR. Debés ingresar un número")
        continue

    #Si la opción no es número del 1 al 5: 
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        print("Opción inválida")
        continue

    #Si quiere salir antes: 
    if opcion == "5":
        print("Sistema cerrado")
        break

    # ======================
    # RESERVAR TURNO
    # ======================
    if opcion == "1":
        while True:  
            #Ingreso de día:
            dia_turno = input("Día (1=Lunes, 2=Martes): ")

            if not dia_turno.isdigit():
                print("Ingresá un número válido")
                continue

            if dia_turno != "1" and dia_turno != "2":
                print("Día inválido")
                continue
            
            #Ingreso de nombre:
            nombre_paciente = input("Nombre del paciente: ")

            if not nombre_paciente.isalpha():
                print("Nombre inválido")
                continue

            #Guardando registro:
            #Guardo en lunes:
            if dia_turno == "1":
                #Verifico repetido:
                if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                    print("Paciente ya registrado")
                    continue

                elif lunes1 == "":
                    lunes1 = nombre_paciente

                elif lunes2 == "":
                    lunes2 = nombre_paciente

                elif lunes3 == "":
                    lunes3 = nombre_paciente

                elif lunes4 == "":
                    lunes4 = nombre_paciente

                else:
                    print("No hay turnos disponibles")
                    break

                print("Turno asignado")
                break

            #Guardar en día martes:
            elif dia_turno == "2":
                #Verifico repetido:
                if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                    print("Paciente ya registrado")
                    continue

                elif martes1 == "":
                    martes1 = nombre_paciente

                elif martes2 == "":
                    martes2 = nombre_paciente

                elif martes3 == "":
                    martes3 = nombre_paciente

                else:
                    print("No hay turnos disponibles")
                    break

                print("Turno asignado")
                break

    # ======================
    # CANCELAR TURNO
    # ======================
    elif opcion == "2":
        while True: 
            dia_turno = input("Día (1=Lunes, 2=Martes): ")

            if dia_turno != "1" and dia_turno != "2":
                print("Día inválido")
                continue

            nombre_paciente = input("Nombre del paciente: ")

            if not nombre_paciente.isalpha():
                print("Nombre inválido")
                continue

            #Cancelar en lunes:
            if dia_turno == "1":
                if nombre_paciente == lunes1:
                    lunes1 = ""
                elif nombre_paciente == lunes2:
                    lunes2 = ""
                elif nombre_paciente == lunes3:
                    lunes3 = ""
                elif nombre_paciente == lunes4:
                    lunes4 = ""
                else:
                    print("Paciente no encontrado")
                    continue

                print("Turno cancelado")
                break

            #Cancelar en día martes:
            elif dia_turno == "2":
                if nombre_paciente == martes1:
                    martes1 = ""
                elif nombre_paciente == martes2:
                    martes2 = ""
                elif nombre_paciente == martes3:
                    martes3 = ""
                else:
                    print("Paciente no encontrado")
                    continue

                print("Turno cancelado")
                break

    # ======================
    # MOSTRAR AGENDA
    # ======================
    elif opcion == "3":
        dia_turno = input("Día (1=Lunes, 2=Martes): ")

        if dia_turno == "1":  #Lunes
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

        elif dia_turno == "2":  #Martes
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

        else:
            print("Día inválido")

    # ======================
    # RESUMEN GENERAL
    # ======================
    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        #Primero cuento los ocupados:
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        #Ahora sí el resumen: 
        print("Lunes ocupados:", ocupados_lunes, "Disponibles:", 4 - ocupados_lunes)
        print("Martes ocupados:", ocupados_martes, "Disponibles:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")
            
