cade = input("Introduzca su nombre:\n")
print(f"1. {cade.lower()}")
a = len(cade)-1
cade2 = cade[0:2].upper() + cade[2:len(cade)-2].lower() + cade[a-1:].upper()
print(f"2.{cade2}")
op = int(input("1. Para vocales mayúsculas / 2. Para consonantes mayúsculas."))
voc = "aeiou"; cade3=""

for i in range(len(cade)):
        if cade[i].lower() in voc:
            cade3 += cade[i].upper()
        else:
            cade3 += cade[i].lower()

if op == 1:
    print(cade3)
else:
    print(cade3.swapcase())