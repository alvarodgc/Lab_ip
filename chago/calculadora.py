
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    resultado = a + b
elif operacion == "-":
    resultado = a - b
elif operacion == "*":
    resultado = a * b
elif operacion == "/":
    if b == 0:
        resultado = "Error: División por cero"
    else:
        resultado = a / b

print("El resultado es:", resultado)


