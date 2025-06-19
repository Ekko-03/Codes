personas={
    1:{"nombre": "Liam neeson",
       "telefono": 876765454,
       "estadocivil":"Soltero",
       "ciudadano":True},
    2:{"nombre": "Christian bale",
       "telefono": 892810984,
       "estadocivil": "Casado",
       "ciudadano": True},
    3:{"nombre": "Jane Doe",
       "telefono": 789798731,
       "estadocivil": "Soltera",
       "ciudadano": True},
    4:{"nombre": "Jhon Doe",
       "telefono": 154791947,
       "estadocivil": "Casado",
       "ciudadano": True},
}
while True:
    try:
        print('''
        1.-Ingresar persona
        2.-Mostrar listado
        3.-Actualizar persona
        4.-Borrar persona
        5.-Salir
        ''')
        op=int(input("Seleccione una opcion "))
        match op:
            case 1:
                nombre=input("Ingrese el nombre de la persona: ")
                telefono=int(input("Ingrese el telefono: "))
                ecivil=int(input("1.-Casado, 2.-Soltero "))
                if ecivil==1:
                    est="Casado"
                else:
                    est="Soltero"
                ciudadania=input("Es ciudadano?: 1.-Si, 2.-No ")
                if ciudadania==1:
                    ciu=True
                else:
                    ciu=False
                ld=len(personas)+1
                personas[ld]={"nombre": nombre,
                            "telefono": telefono,
                            "estadocivil": est,
                            "ciudadano": ciu}
            case 2:
                for n,persona in personas.items():
                    print(n, personas)
            case 3:
                for n,persona in personas.items():
                    print(n, personas)
                act=int(input("Seleccione cual desea actualizar"))
                print('''
                    1.-Nombre
                    2.-Numero de telefono
                    3.-Estado civil
                    4.-Ciudadania
                    5.-Salir
                    ''')
                dato=int(input("que dato quiere actualizar?"))
                match dato:
                    case 1:
                        n=input("Ingrese el nombre nuevo")
                        dat="Nombre"
                        personas[act][dat]=n
                    case 2:
                        num=int(input("Ingrese el nuevo numero"))
                        dat="Telefono"
                        personas[act][dat]=num
                    case 3:
                        ecivil=int(input("1.-Casado, 2.-Soltero "))
                        if ecivil==1:
                            est="Casado"
                        else:
                            est="Soltero"
                        dat="EstadoCivil"
                        personas[act][dat]=ecivil
                    case 4:
                        ciudadania=input("Es ciudadano?: 1.-Si, 2.-No ")
                        if ciudadania==1:
                            ciu=True
                        else:
                            ciu=False
                        dat="Ciudadano"
                        personas[act][dat]=ciudadania
                    case 5:
                        break
                    case _:
                        print("Seleccione una opcion correcta")
            case 4:
                for n,persona in personas.items():
                    print(n, personas)
                borrar=int(input("ingrese cual quiere eliminar: "))
                del personas[borrar]
                print(f"La persona {borrar} fue eliminada")
            case 5:
                break
            case _:
                print("seleccione una opcion correcta")
    except Exception as e:
        print("el error es: ", e)


            
