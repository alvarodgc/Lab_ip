while True:
    nombre = input("Nombre: ").strip()
    nombre
    #print(nombre)

    if nombre and nombre.replace(" ", "").isalpha():
        break

    print("Usa letras y no dejes el nombre vacio.")

nombre_normalizado = nombre.title()  
print(f"Hola, {nombre_normalizado}")