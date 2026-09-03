for numero in range(0, 7, 3):    # for con range
    cuadrado = numero ** 2
    print(numero, cuadrado)   #for sirve


materias = ["Python", "Linux", "Interfaces"]     #for con listas
for posocopn, materia in enumerate (materias, start=1):
    print(f"{posocopn}. {materia}")

for materia in materias:  # 
    print(materia)
cadena = "0123456789ABCDEF"
for letra in cadena:  
    print(letra)

for i in range(len(cadena)):
    print(cadena[i])

