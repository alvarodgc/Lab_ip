operador = input ("Ingrese un operador (+,-,*,/): ")     
o1 = (input("Ingrese el primer numero: "))     #no es necesario poner el int
o2 = int(input("Ingrese el segundo numero: "))
resultado = str(o1) + operador + str(o2)
resultado = eval(resultado)
print(resultado)