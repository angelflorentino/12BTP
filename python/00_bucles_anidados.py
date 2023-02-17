# ejercicios del 17/02/23

# impresión de un triángulo rectángulo con asteriscos con altura proporcionada por el usuario.

n = int(input("Introduzca un número N: "))

for i in range(n): # este bucle sirve para iterar la cantidad de veces indicada por el usuario.
    for i2 in range(i+1):   # este bucle iterará hasta el valor almacenado en i, aumentado en 1 por la resta que hace el for.
        print("*", end=" ") # esta instrucción imprimirá el asterisco sin salto de línea, la cantidad de veces que valga i.
    print("")   # aquí se hará el salto de línea, cada vez que termine de iterar el bucle i2.

# impresión de un triángulo rectángulo con números que vuelven a comenzar por cada fila.

n = int(input("Introduzca un número N: "))

for i in range(n):
    for i2 in range(i+1):
        print(i2+1, end=" ")    # este es el cambio acá, se imprime i2+1, que cada vez que finaliza se formatea a 0, y llega hasta el valor que se tenga de i.
    print("")

# impresión de un triángulo rectángulo cuyas filas son el número de la iteración.

n = int(input("Introduzca un número N: "))

for i in range(n+1):
    for i2 in range(i):
        print(i, end=" ")   # acá se imprime i, que corresponde también al número de elementos que se imprimirán, el sub-bucle imprime i, i veces.
    print("")