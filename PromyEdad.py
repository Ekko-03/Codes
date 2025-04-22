# sacar promedio 3 numeros 
print("ingrese 3 numeros para sacar su promedio")
n1=int(input("ingrese un numero "))
n2=int(input("ingrese un numero "))
n3=int(input("ingrese un numero "))
prom=(n1+n2+n3)/3
print("el promedio es", prom)

# promedio con for
print("ingrese numeros para sacar su promedio")
cantN=int(input())
suma=0
for i in range(cantN):
    print("Ingrese la primera nota",i +1)
    nota=float(input())
    suma=suma+nota
    # suma+=nota
prom=suma/cantN
print("Su promodedio es ", prom)
if prom>=4.0:
    print("usted aprobo")
elif prom<4.0:
    print("usted reporbo")

# Edad else
print("ingrese su edad")
edad=int(input("ingrese su edad"))

if edad>=18:
    print("usted es mayor de edad")
else:
    print("usted es menor de edad")

edad=int (input("ingrese su edad: "))

# Edad if

if edad<12:
    print("tiene",edad,"por tanto es un niño")
elif edad>= 12 and edad<=17:
    print("tiene", edad,"por tanto es un adolescente")
else:
    print("tiene", edad, "por tanto es mayor de edad")

a