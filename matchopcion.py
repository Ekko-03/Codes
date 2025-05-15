
def suma ():
    n1=int(input("ingrese un Numero:  "))
    n2=int(input("ingrese un Numero:  "))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("ingrese un Numero:  "))
    n2=int(input("ingrese un Numero:  "))
    print("El resultado de la resta es", n1-n2)
def mult():
    n1=int(input("ingrese un Numero:  "))
    n2=int(input("ingrese un Numero:  "))
    print("El resultado de la multiplicacion es", n1*n2)
def div():
    n1=int(input("ingrese un Numero:  "))
    n2=int(input("ingrese un Numero:  "))
    print("El resultado de la division es", n1/n2)

def calcu():
    while True:
        op=int(input('''Seleccione una opcion
                    1.- Suma
                    2.- Resta
                    3.- Multiplicar
                    4.- Division
                    5.- Salir
                    '''))
        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicar")
                mult()
            case 4:
                print("Division")
                div()
            case 5:
                print("Saliendo del sistema")
                break
            case _:
                print("Opcion invalida")
# # calcu()

suma2(7,9,12)

def seleccionar_personaje(jugador):
    while True:
        print(f"{jugador}, selecciona tu personaje:")
        op = int(input('''Seleccione un personaje: 
        1.- Scorpion 
        2.- SubZero 
        3.- Jhonny Cage 
        4.- Sonya Blade 
        5.- Kitana 
        6.- Milenna 
        7.- Jade 
        8.- Salir del juego 
        '''))
        match op:
            case 1:
                personaje = "Scorpion"
            case 2:
                personaje = "SubZero"
            case 3:
                personaje = "Jhonny Cage"
            case 4:
                personaje = "Sonya Blade"
            case 5:
                personaje = "Kitana"
            case 6:
                personaje = "Milenna"
            case 7:
                personaje = "Jade"
            case 8:
                print("Cerrando el juego...")
                break
            case _:
                print("Selección inválida. Intenta nuevamente.")
                continue
        return personaje
    
Pj1 = input("Ingresa el nombre del primer jugador: ")
Pj2 = input("Ingresa el nombre del segundo jugador: ")

personaje_pj1 = seleccionar_personaje(Pj1)
personaje_pj2 = seleccionar_personaje(Pj2)

print(f"El combate será entre ({Pj1}) {personaje_pj1} y ({Pj2}) {personaje_pj2}")

