# otros ejercicos de for

# Perros de caza
# Pida al usuario la cantidad de perros
# Muestre cual es la cuota minima de conejos
# lugo consulte cuantos conejos trajo
# si el perro tran¿jo la cantidad minima
# cumplio la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no





import random
# while True:
#     try:
#         cant=int(input("ingrese un numero de perros: "))
#         cuota=3
#         cumple=0
#         for i in range(cant):
#             con=random.randint(0,5)
#             print(f"El perro {i+1} trajo {con} conejos")
#             if con>=cuota:
#                 print("El perro gana filete")
#                 cumple+=1
#             else:
#                 print("Se queda sin carne de res")
#         print(f" La cantida de perro que cuplieron la cuota es {cumple}")
#         print(f" La cantida de perro que NO cuplieron la cuota es {cant-cumple}")
#         break
#     except Exception:
#         print("Solo se aceptan numeros enteros")

# try:
#     #codigo a aejecutar
#     print("Ejecuta algo")
# except Exception:
#     # mensaje de error
#     print("Error")

# cant=int(input("ingrese un numero de perros: "))


# Quiere pasar el ramo?
# Pregunte la cantidad de rojos en el curso
# Los talleres hay en el semestre son 4
# Por cada taller asistido obtiene 0.3 decimas
# Si el alumno tiene mas de 1 punto
# tiene la bendicion dlel profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# Muestre si aprueba o reprueba .

# rojos=int(input("Diga la cant de rojos: "))
# talleres=4
# tDecimas=0

# for r in range(rojos):
#     for t in range(talleres):
#         asist=input(f"Asistio al taller numero {t+1}? si/no: ")
#         if asist.lower()=="si":
#             tDecimas+=0.3
#     if tDecimas>=1:
#         print(" Tiene la bendicion del profe")
#     else:
#         print("Nada mas que hacer ")
#     nf=float(input("Ingrese su nota final"))
#     nf+=tDecimas
#     print(f"su nota final es {nf}")
#     if nf>=4:
#         print("El alumno aprobó")
#     else:
#         print("El alumno reprobó")

# while True:
#     print("Menú de Opciones:")
#     print("1. Realizar acción 1")
#     print("2. Realizar acción 2")
#     print("3. Salir")
#     opcion = input("Selecciona una opción (1-3):")
#     # Opcion de menu con if y elif
#     if opcion == "1":
#         print("Has seleccionado la opción 1.")
#         # Código para la acción 1
#     elif opcion == "2":
#         print("Has seleccionado la opción 2.")
#         # Código para la acción 2
#     elif opcion == "3":
#         print("Saliendo del programa.")
#         break
#     else:
#         print("Opción no válida.")
#     # opcion de menus con if secuenciales
#     if opcion == "1":
#         print("Has seleccionado la opción 1.")
#         # Código para la acción 1
#     if opcion == "2":
#         print("Has seleccionado la opción 2.")
#         # Código para la acción 2
#     if opcion == "3":
#         print("Has seleccionado la opción 3.")
#         # Código para la acción 3
#     # Opcion de menu con match
#     match opcion:

#         case "1":
#                 print("Has seleccionado la opción 1.")
#                 # Código para la acción 1        
#         case "2":
#                 print("Has seleccionado la opción 1.")
#                 # Código para la acción 1        
#         case "3":
#                 print("Has seleccionado la opción 1.")
#                 # Código para la acción 1
#         case _:
#               print("Defecto")





def pagolavado():
    global ventas, autos, full, standard, basico
    tipodelavado=int(input('''elija su tipo de lavado:
                           1. FUll $15.000
                           2. STANDARD $10.000
                           3. BASICO $7.000
                           '''))
    match tipodelavado:
        case 1:
            ventas+=15000
            autos+=1
            full+=1
            print("selecciono lavado FULL")
        case 2:
            ventas+=10000
            autos+=1
            standard+=1
            print("selecciono lavado STANDARD")
        case 3:
            ventas+=7000
            autos+=1
            basico+=1
            print("selecciono lavado BASICO")
        case _:
            print("opcion invalida")
def ventasdia():
    print(f'''ventas totales ${ventas}
    Num de autos {autos}''')
    if full>=1:
        print("el monto mas alto fue de $15.000")
    elif standard>=1 and full==0:
        print("el monto mas alto fue de $10.000")
    elif basico>=1 and standard==0 and full==0:
        print("el monto mas alto fue de $7.000")
ventas=0
autos=0
full=0
standard=0
basico=0
while True:
    op=int(input(''''elija que quiere hacer:
                1.pago de lavado
                2.ver ventas
                3.salir
                 '''))
    match op:
        case 1:
            pagolavado()
        case 2:
            ventasdia()
            if ventas==0:
                print("usted no ha tenido ningun cliente")
        
        case 3:
            print("hasta la vista")
            break
        case _:
            print("ingrese una opcion valida")


