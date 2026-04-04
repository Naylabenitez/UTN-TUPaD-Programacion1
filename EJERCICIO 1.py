#EJERCICIO 1: 
#Primero solicité el nombre del cliente
nombre_cliente = input("Nombre de cliente: ").strip()
#Aplico la regla de no admitir vacíos ni entradas que no sean alfabéticas
while nombre_cliente == "":
    print("ERROR. No ingresaste nombre")
    nombre_cliente = input("Nombre de cliente: ").strip()    
while not nombre_cliente.isalpha():
    print("ERROR. El nombre debe tener solo letras")
    nombre_cliente = input("Nombre de cliente: ").strip()
#Esto nomás es para probar la salida durante el proceso
print("Nombre registrado")
#Aplico lo mismo con cantidad de productos, no 0 ni entradas que no sean numéricas
cantidad_productos = input("Cantidad de productos: ").strip()
while not cantidad_productos.isdigit():
    cantidad_productos = input("Por favor ingresa una cantidad numérica: ").strip()
while cantidad_productos == "0":
    cantidad_productos = input("Por favor ingresa una cantidad mayor a 0: ").strip()
#Lo convierto a entero y coloco una señal para la salida.
cantidad_productos = int(cantidad_productos)
print ("Cantidad registrada")
total_sin_descuento = 0
total_con_descuento = 0 
#puse un for que se repite según la cantidad de productos que pusimos
for i in range(cantidad_productos):
    print(f"\nProducto {i + 1}")
    
    precio = int(input(f"Ingresá el precio del producto {i + 1}: "))
    descuento = input("¿Tiene descuento? S/N: ").strip().upper()
    
    precio_original = precio
    
    if descuento == "S":
        precio = int(precio * 0.9)
    
    total_sin_descuento += precio_original
    total_con_descuento += precio
ahorro_total = total_sin_descuento - total_con_descuento
promedio_por_producto = total_con_descuento / cantidad_productos
#Ahora lo que va a ver el usuario:
print(f"\nTotal sin descuentos: {total_sin_descuento}")
print(f"Total con descuentos: {total_con_descuento}")
print(f"Ahorro total: {ahorro_total}")
print(f"Promedio por producto: {promedio_por_producto:.2f}")
