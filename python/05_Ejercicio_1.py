c = input("Introduzca una cadena de carácteres: ")
x = len(c)
cc2 = "";css = c[0]; voc = "aeioua";vc = ""; vocm = "AEIOU"

print(f"1. {c[0:2]}. Impresión de los dos primeros.\n")

print(f"2. {c[x-3:x]}. Impresión de los tres últimos. \n")
for i in range(0,len(c),2):
    cc2 += c[i]
print(f"3. {cc2}. Impresión cada dos carácteres. \n")

for i in range(len(c)):
    if c[i] == " ":
        css += c[i+1]
print(f"3. {css}. Impresión de la inicial de cada palabra. \n")
