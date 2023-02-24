cad = input("Introduzca una cadena: \n")
pal = ""
for i in range(len(cad)-1,-1,-1):
    pal += cad[i]
if cad.lower() == pal.lower():
    print("Es palíndromo.")
else:
    print("No es palíndromo.")