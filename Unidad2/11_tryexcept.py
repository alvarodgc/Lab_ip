while True:
    try:
        edad = int(input("Edad: "))

        if 0 <= edad <= 120:
            break

        print("La edad debe estar entre 0 y 120 años.")
    except ValueError:
        print("Debes ingresar un número entero.")

print(f"Edad registrada: {edad} años.") 