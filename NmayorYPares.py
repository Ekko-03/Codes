# Numero mayor 
n1=int(input("ingrese un numero"))
n2=int(input("ingrese otro numero"))
n3=int(input("ingrese otro numero"))

if n1>n2 and n1>n3:
    print("el numero", n1, "es el mayor")
if n2>n3:
    print("el numero", n2, "es el mayor")
else:
    print ("el numero", n3, "es el mayor")


# Pares y impares
n1=int(input("ingrese un numero"))

if n1 % 2==0:
    print("el numero es par")
else:
    print("el numero es impar")

a