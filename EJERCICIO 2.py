#EJERCICIO 2: 
#primero defino las credenciales OK (Coloco las del requisito por si acaso):
usuario_correcto = "alumno"
clave_correcta = "python123"

while True:  # sistema completo

    login_ok = False

    # LOGIN
    for i in range(3):
        intento_usuario = input("Ingresá usuario: ")
        intento_clave = input("Ingresá clave: ")

        if intento_usuario == usuario_correcto and intento_clave == clave_correcta:
            print("Credenciales correctas")
            login_ok = True
            break
        else:
            print("Credenciales incorrectas")
            if i == 2:
                print("Cuenta bloqueada")
                exit()

    # MENÚ
    if login_ok:
        while True:
            print("\nMenú:")
            print("1. Ver estado de inscripción")
            print("2. Cambiar clave")
            print("3. Ver mensaje motivacional")
            print("4. Salir")

            opcion = input("Elegí una opción: ")

            if not opcion.isdigit():
                print("ERROR. Debés ingresar un número")
                continue

            if opcion not in "1234":
                print("ERROR. Opción fuera de rango")
                continue

            if opcion == "1":
                print("Estado de inscripción: Inscripto")

            elif opcion == "2":
                nueva_clave = input("Ingresá nueva clave: ")

                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres")
                    continue

                confirmacion = input("Confirmá la nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente")
                else:
                    print("Las claves no coinciden")

            elif opcion == "3":
                print("El éxito es la suma de pequeños esfuerzos repetidos día tras día.")

            elif opcion == "4":
                print("Cerrando sesión...\n")
                break  # vuelve al login