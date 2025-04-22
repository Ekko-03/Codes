# Votos
c1="Coyote"
c2="Porky"
cantvotos1=0
cantvotos2=0

cantV=int(input("ingrese la cant de votantes :"))
suma=0 
for i in range(cantV):
    # print("por quien votara?: 1.-", c1, ", 2.- " ,c2)
    print(f"por quien votara?: 1.-{c1}, 2.- {c2}")
    voto=input()

    if voto=="1":
        print(f"usted voto por {c1}")
        cantvotos1+=1
    else:
        print(f"usted voto por {c2}")
        cantvotos2+=1
print(f"la cantidad de votos de {c1} es {cantvotos1}")
print(f"la cantidad de votos de {c2} es {cantvotos2}")

if cantvotos1>cantvotos2:
    print(f"gano {c1}")
elif cantvotos2>cantvotos1:
    print(f"gano {c2}")
else:
    print("votacion empatada")


# # caracteres for
# frase=input("ingrese una frase: ")
# caracteres=0

# for i in frase:
#     caracteres+=1
# print(f"cantidad de caracteres {caracteres}" )

# # caracteres len
# frase=input("ingrese una frase: ")
# cont=len(frase)
# print(f"cantidad de caracteres {cont}" )

