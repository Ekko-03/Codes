

"""
menu de opciones 
1.- agregar elemento a la lista
2.- eliminar elemento de la lista
3.- mostrar cada uno de los elemento de la lista de forma ordenada
4.- cerrar sistema



1.- agregar elemento a la lista  : el sistema de solicitar un str 
y agregarlo al final de la lista

2.- eliminar elemento de la lista : el sistema debe listar cada producto en forma
de secuencia iniciando en 1, por ejmplo de la lista = [a,b,c]
se tienen que listar
1.-a
2.-b
3.-c

el usuario elige uno de los 3 con su número correspondiente y el sistema debe eliminar 
el producto de la lista

3- listar cada uno de los elementos de la lista de manera ordenada


#append(E) -> Agrega un elemento al final de la lista
#pop(int)  -> elimina un elemento de la lista del index especificado
#remove(E) -> elimina la primera coincidencia del E en la lista
# funcion  len()  -> retorna un int como la cantidad de E en la lista
# """
from ejerciciovalidaciones import validar_numero,saludar
from os import system

system("cls")
if "h".isdigit():
    print("se puede transformar")
    a =  int("4")
else:
    print("no se puede ")
saludar()
lista_productos = ["tomate","café","chocolate","pan con queso"]
while True:
    print("MENU DE OPCIONES")
    print("1.-agregar producto")
    print("2.-eliminar un producto") #validar
    print("3.-listar los productos ordenados")
    print("4.-salir del sistema")
    
    opc = validar_numero(1,4,"opcion")
    match opc:
        case 1:
            producto = input("ingrese nombre del producto: ")
            lista_productos.append(producto)
            print(f"producto {producto} agregado exitosamente a la lista")
            input("presione enter para continuar ...")
            system("cls")
        case 2:
            if len(lista_productos) == 0:
                print("INFO la lista está vacia ! ")
                input("presione enter para continuar ...")
                system("cls")
            else:
                cont = 1
                for i in lista_productos:
                    print(f"{cont}.-{i}")
                    cont +=1
                aux = validar_numero(1,len(lista_productos),"eliminar →")-1
                print(f"producto {lista_productos[aux]} eliminado exitosamente ! ")
                lista_productos.pop(aux)
                input("presione enter para continuar ...")
                system("cls")
        case 3:
            cont = 1
            for i in lista_productos:
                print(f"{cont}.-{i}")
                cont +=1
            input("presione enter para continuar ...")
            system("cls")
        case 4:
            print("Saliendo del sistema")
            break
        case _:
            print("ERROR ingreso un valor no valido ! ")
            input("presione enter para continuar ...")
            system("cls")
        