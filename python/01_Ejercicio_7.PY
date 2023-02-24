cad = input("Introduzca una cadena: \n").lower()
car1 = input("Introduzc el carácter a buscar: ").lower()
car2 = input("Introduzc el carácter reemplazo: ").lower()
cadr = ""
for i in range(len(cad)):
    if cad[i] == car1:
        cadr += car2
    else:
        cadr += cad[i]

print(cadr)