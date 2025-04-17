# sacar promedio 3 numeros 
print("ingrese 3 numeros para sacar su promedio")
n1=int(input("ingrese un numero "))
n2=int(input("ingrese un numero "))
n3=int(input("ingrese un numero "))
prom=(n1+n2+n3)/3
print("el promedio es", prom)

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
