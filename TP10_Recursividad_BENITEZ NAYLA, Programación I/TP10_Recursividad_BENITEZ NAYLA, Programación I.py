# ==========================================
# TP10_Recursividad_BENITEZ NAYLA
# Programación I
# ==========================================1===================================
#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(n):

    # Cuando llega a 0 termina la recursión
    if n == 0:
        return 1

    # Multiplica el número actual por el factorial del anterior
    return n * factorial(n - 1)


num = int(input("Ingrese un número para calcular factoriales: "))

print("\nFactoriales:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


# ==========================================2===================================
#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique.

def fibonacci(n):

    # Los dos primeros valores de la serie
    if n <= 1:
        return n

    # Cada término es la suma de los dos anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)


pos = int(input("\nIngrese una posición para Fibonacci: "))

print("Serie Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()


# ==========================================3===================================
#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def potencia(base, exponente):

    # Todo número elevado a 0 es 1
    if exponente == 0:
        return 1

    # Multiplica la base tantas veces como indique el exponente
    return base * potencia(base, exponente - 1)


base = int(input("\nIngrese la base: "))
exp = int(input("Ingrese el exponente: "))

print("Resultado:", potencia(base, exp))


# ==========================================4===================================
#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):

    # Cuando queda 0 o 1 ya está representado en binario
    if n < 2:
        return str(n)

    # Divide por 2 y agrega el resto obtenido
    return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("\nIngrese un número decimal: "))

print("Binario:", decimal_a_binario(numero))


# ==========================================5===================================
#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
#     Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):

    # Si queda una letra o ninguna, es palíndromo
    if len(palabra) <= 1:
        return True

    # Si los extremos son distintos, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False

    # Vuelve a comparar quitando la primera y la última letra
    return es_palindromo(palabra[1:-1])


texto = input("\nIngrese una palabra: ")

print("¿Es palíndromo?", es_palindromo(texto))


# ==========================================6===================================
#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
#     Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):

    # Si tiene un solo dígito, ese es el resultado
    if n < 10:
        return n

    # Suma el último dígito y continúa con el resto del número
    return (n % 10) + suma_digitos(n // 10)


numero = int(input("\nIngrese un número: "))

print("Suma de dígitos:", suma_digitos(numero))


# ==========================================7===================================
#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
 
#      Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

def contar_bloques(n):

    # Cuando queda un solo nivel, retorna 1 bloque
    if n == 1:
        return 1

    # Suma los bloques del nivel actual con los niveles superiores
    return n + contar_bloques(n - 1)


nivel = int(input("\nIngrese bloques del nivel inferior: "))

print("Total de bloques:", contar_bloques(nivel))


# ==========================================8===================================
#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
#      Ejemplos: 
#contar_digito(12233421, 2)   → 3   
#contar_digito(5555, 5)       → 4   
#contar_digito(123456, 7)     → 0   

def contar_digito(numero, digito):

    # Si ya no quedan dígitos por analizar, termina
    if numero == 0:
        return 0

    # Verifica si el último dígito coincide con el buscado
    aparece = 1 if numero % 10 == digito else 0

    # Continúa analizando el resto del número
    return aparece + contar_digito(numero // 10, digito)


numero = int(input("\nIngrese un número: "))
digito = int(input("Ingrese el dígito a buscar: "))

print("Cantidad de apariciones:",
      contar_digito(numero, digito))
