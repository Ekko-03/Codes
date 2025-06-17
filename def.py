# # IVA + DESCUENTO
# def cal_iva(n):
#     return n*0.19

# def cal_desc(precio, porc):
#     return precio*(porc/100)

# # # diccionario
# productos=[
#     {"nombre":"Portamina", "precio": 400},
#     {"nombre":"Goma", "precio": 200},
#     {"nombre": "Estuche", "precio": 1600}
# ]
# # print(productos[0]["precio"])

# # 

productos=[
    {"nombre":"Portamina", "precio": 400},
    {"nombre":"Goma", "precio": 200},
    {"nombre": "Estuche", "precio": 1600}
]
def muestra_lista(lista):
    for n, productos in enumerate(lista):
        print(n+1, productos["nombre"], productos["precio"])

def agregar():
    nombre=input("Ingrese el nombre del articulo: ")
    precio=int(input("Ingrese el Precio: "))
    productos.append({"nombre":nombre,"precio":precio})

def actualizar():
    act=int(input("Seleccione cual desea actualizar"))
    nombre=input("ingrese el nombre del articulo")
    precio=int(input("ingrese el nombre del precio"))
    productos[act-1]["nombre"]=nombre
    productos[act-1]["precio"]=precio

def eliminar():
    borrar=int(input("ingrese cual quiere eliminar: "))
    productos.pop(borrar-1)

while True:
    try:
        print('''
              1.-Agregar articulo
              2.-Borrar articulo
              3.-Actualizar articulo
              4.-Mostrar listado de productos
              5.-Salir
              ''')
        op=int(input("Seleccione una opcion "))
        match op:
            case 1:
                agregar()
            case 2:
                muestra_lista(productos)
                eliminar()
            case 3:
                muestra_lista(productos)
                actualizar()
            case 4:
                muestra_lista(productos)
            case 5:
                break
            case _:
                print("opcion invalida")
    except Exception as error:
        print("el error es :", error )
            


        

