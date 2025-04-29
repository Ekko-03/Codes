# # a=int(input())
# # for i in range (1,10001):
# #      print(f"{i}x{a}={i*a}")

# # edad=-1
# # while(edad<0 or edad>100):
# #     edad=int(input(""))
# #     if(edad<0 or edad>100):
# #         print("Error,fuera de rango")
# # print("ingresado exitosamente")
# # print(edad)


# num=int(input("ingrese un numero: "))
# if num%2==0:
#     print("par")
# else:
#     print("impar")
# print("mostrar numero pares")
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)
# print("mostrar numeros impares")
# for i in range(1,num+1):
#     if i%2!=0:
#         print(i)


# cont=0
# total=0
# opc=0
# while opc !=2:
#     print("1-agregar nuevo numero")
#     print("2-salir")
#     opc = int(input("->"))
#     if(opc==1):
#         num=int(input("ingrese un numero: "))
#         cont+=1
#         total+=num
# print(f"la cantidad de numeros ingresados son{cont}")
# print(f"la suma de cada uno de ellos es{total}")

# from random import randint
# a=0
# b=0
# r = a*b
# while r < 50:
#     a = int(input("ingrese el valor de a: "))
#     b = randint(2,8)
#     r = a*b
#     print(f"el numero aleatorio es {b}")
#     print(f"la multiplicacion entre{a} x {b} = {r} ")
#     if r < 50:
#         print("intente nuevamente!")
# print("LOGRO LA META!")

num = -1
while(num<0):
    num=int(input("ingrese un numero positivo"))
    if(num < 0):
        print("Error, ingrese un numero menor a 0. vuelva a intentarlo")
print("numero ingresado exitosamente!")
num *= 5 
num -= 8
num += 3
num /= 2
print(f"el valor resultante es {num}")