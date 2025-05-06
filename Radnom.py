import random
print("ingrese 2 numeros")
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese un numero mayor al anterior: "))
while n1>n2:
    print("El segundo numero no puede ser menor")
    n2=int(input("ingrese el numero 2 nuevamente"))
r = random.randint(n1,n2)
print(f"el numero aleatorio entre los 2 numeros que ingresaste es: {r}")
print("▄"*r)

