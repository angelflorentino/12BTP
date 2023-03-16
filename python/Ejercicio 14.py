# Creamos las listas vacías para los productos y precios
productos = []
precios = []
isv = []
total = []
descuento = []

# Pedimos al usuario que ingrese los nombres y precios de los 10 productos
for i in range(2):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos.append(producto)
    precios.append(precio)

# Creamos la lista con los descuentos (10% de cada precio)
for i in range(2):
    descuento.append(precios[i]*0.10)

# Calculamos el ISV (15% de la suma de precios)
for i in range(2):
    isv.append(precios[i]*0.15)

# Calculamos el total a pagar (suma de precios - descuentos + ISV)
for i in range(2):
    total.append(precios[i] - descuento[i] + isv[i])

# Imprimimos los resultados
print(f"Productos: {productos}")
print(f"Precios:   {precios}")
print(f"Descuento: {descuento}")
print(f"ISV:       {isv}")
print(f"Total:     {total}")