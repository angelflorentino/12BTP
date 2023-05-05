import sqlite3 as sq

conexion = sq.connect("censo.db")
cursor = conexion.cursor()

try:
    conexion.execute("""create table poblacion(
    id integer primary key,
    apellido text,
    nombre text,
    edad integer,
    ciudad text,
    telefono text);""")
    print("Tabla creada.")
except:
    cursor.execute("delete from poblacion")
    print("Tabla conectada")

cursor.execute("""insert into poblacion(id,apellido,nombre,edad,ciudad,telefono)
values(1201,"Bario","Paka",58,"Siguatepeque","2773-1272"),
(1520,"Fernández","Chente",78,"La Paz","2774-7427"),
(1314,"Valencia","Luismiguel",50,"Comayagua","2772-2772"),
(1010,"Esmeralda","Perla",26,"Comayagua","2772-7227"),
(1311,"Negrete","Virginia",32,"Siguatepeque","2773-7723"),
(1510,"Arguijo","Arlen",30,"La Paz","2774-4277");""")

print("\nTodos los registros:\n")
cursor.execute("Select * from poblacion")
tdr = cursor.fetchall()
for i in tdr:
    print(i)

nom = input("\nIngrese nombre filtro: ")
print("\n")
cursor.execute(f"select id, apellido, nombre, edad from poblacion where nombre like '%{nom}%';")
nf = cursor.fetchall()
if nf:
    for i in nf:
        print(i)
else:
    print("No registros encontrados.")

ciu = input("\nIngrese ciudad filtro: ")
print("\n")
cursor.execute(f"select nombre, apellido from poblacion where ciudad like '%{ciu}%'")
cf = cursor.fetchall()
if cf:
    for i in cf:
        print(i)
else:
    print("No registros encontrados.")


edad = int(input("\nIngrese la edad límite: "))
cursor.execute(f"select * from poblacion where edad < {str(edad)};")
efa = cursor.fetchall()
if efa:
    for i in efa:
        print(i)
else:
    print(f"No hay registros menores a {edad}")

conexion.commit()
conexion.close()