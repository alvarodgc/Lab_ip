while True:
    while True:
        edad = int(input("Edad: "))

        if 0 <= edad <= 120 and type(edad) == int:
            break

        print("La edad debe estar entre 0 y 120 años.")
    if type (edad) != int:
        print("Debes ingresar un número entero.")

print(f"Edad registrada: {edad} años.")