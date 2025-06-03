
def validar_numero(minimo,maximo,texto):
    while True:
        try:
            opc = int(input(f"ingrese  {texto} : "))
            if opc < minimo or opc > maximo :
                print("ERROR en rango  ! ")
            else:
                return opc
        except ValueError:
            print("ERROR ingreso otro tipo de dato")
def saludar():
    print("hola")