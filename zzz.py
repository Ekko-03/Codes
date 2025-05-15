precio=0
while True:
    print('''
         1.-ingresar su nombre
        2.-comprar
        3.-sacar boleta
        4.-salir
        ''')
    match op:
        case 1:
            nombre=(input("Ingrese su nombre"))
            print(f"Buenos dias, {nombre} Usted a ingresado al sistema. ¿Que desea hacer?")
        case 2:
            while True:
                print('''Seleccione una opcion
                         1.- Yogurt $1.500
                         2.- Cereal $2.390
                         3.- Pan integral $2.899
                         4.- Jamon $2.250
                         5.- Queso $5.299
                         6.- Mermelada $1.000
                         7.- Mantequilla $2.250
                         8.- Terminar compra
                        ''')
                                 opc=int(input())
                                match opc:
                                    case 1:
                                        print("Usted a agregado Yogurt a su carrito")
                                        precio+=1500
                                    case 2:
                                        print("Usted a agregado Cereal a su carrito")
                                        precio+=2390
                                    case 3:
                                        print("Usted a agregado Pan integral a su carrito")
                                        precio+=2899
                                    case 4:
                                        print("Usted a agregado Jamon a su carrito")
                                        precio+=2250
                                    case 5:
                                        print("Usted a agregado Queso a su carrito")
                                        precio+=5299
                                    case 6:
                                        print("Usted a agregado Mermelada a su carrito")
                                        precio+=1000
                                    case 7:
                                        print("Usted a agregado Mantequilla a su carrito")
                                        precio+=2250
                                    case 8:
                                        print("Terminando compra")
                                        break
                                    case _:
                                        print("Opcion invalida")
                                        total=round(precio*1.19)
        case 3:
            print(f"Buenos dias, {nombre}. El precio total se su compra es: {total}")
        case 4:
            print("Saliendo del sistema")
            break




