#contar caracteres
frase=input("ingrese una frase: ")
cantcar=0
v=0
cons=0
e=0
for i in frase:
    print(i)
    cantcar+=1
    # if i.lower(en minusculas) o i.upper(en mayusculas) in "aeiouáéíóú"
    if i in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        v+=1
    elif i==" ":
       e+=1
    else:
        cons+=1
    


print(f"el total de caracteres es {cantcar}")
print(f"el total de vocales es {v}")
print(f"el total de consonantes es {cons}")

# # While=Mientras
num=10
# # while num<5:
# #     print("Hola")
# #     num+=1

import time

while num>0:
    print(num)
    time.sleep(1)
    num-=1

# Contraseña

clave=3344
intentos=3
password=int(input("ingrese su clave: "))
while clave!=password or intentos==0:
    intentos-=1
    print(f"ERROR, quedan {intentos} intentos")
    pwassword=int(input("ingrese su clave:"))
    if intentos<=1:
        break


if intentos!=0 and clave==password:
    print("usted ingreso al sistema")
else:
    print("ERROR, sistema bloqueado")
