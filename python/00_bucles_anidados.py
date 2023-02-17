# ejercicios del 17/02/23

# impresión de un triángulo rectángulo con asteriscos con altura proporcionada por el usuario.

n = int(input("Introduzca un número N: "))

for i in range(n):
    for i2 in range(i+1):
        print("*", end=" ")
    print("")

# impresión de un triángulo rectángulo con números que vuelven a comenzar por cada fila.

n = int(input("Introduzca un número N: "))

for i in range(n):
    for i2 in range(i+1):
        print(i2+1, end=" ")
    print("")

# impresión de un triángulo rectángulo cuyas filas son el número de la iteración.

n = int(input("Introduzca un número N: "))

for i in range(n+1):
    for i2 in range(i):
        print(i, end=" ")
    print("")