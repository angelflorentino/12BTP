# Creamos las listas vacías para los productos y precios
productos = []
precios = []

# Pedimos al usuario que ingrese los nombres y precios de los 10 productos
for i in range(10):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos.append(producto)
    precios.append(precio)

# Creamos la lista con los descuentos (10% de cada precio)
descuentos = [precio * 0.1 for precio in precios]

# Calculamos el ISV (15% de la suma de precios)
isv = sum(precios) * 0.15

# Calculamos el total a pagar (suma de precios - descuentos + ISV)
total = sum(precios) - sum(descuentos) + isv

# Imprimimos los resultados
print("Productos:", productos)
print("Precios:", precios)
print("Descuentos:", descuentos)
print("ISV:", isv)
print("Total a pagar:", total)
