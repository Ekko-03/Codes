# Listas

#     -6-5-4-3-2-1
lista=[1,5,7,8,9,3]
#      0 1 2 3 4 5
print(lista[3])

# mostrar toda la lista
print(lista)

# Recorer la lista
for num in lista:
    print(num)


# notas

c=0
suma=0
notas=[67,46,70,56]

for nota in notas:
    suma+=nota
    c+=1
prom=suma/c
print("el promedio es", round(prom))

# Recorrer nombres

nombres=["Robin","Noelia","Coni"]
apellidos=["Hood","Maldonado","Chan"]

print(len(nombres))

for i in range(len(nombres)):
    print(f"su nombre es {nombres[i]} {apellidos[i]}")


#Caracteres
frutas=["snadia", "Melon", "Manzana"]
for fruta in frutas:
    print(f"La {fruta} tiene {len(fruta)} caracteres")

autos=["Audi", "Toyota", "BWM", "KIA", "Mercedes"]
for auto in autos:
    print(auto)
    if "a" in auto.lower():
        print("la marca tiene una a")
    else:
        print("No hay a")  