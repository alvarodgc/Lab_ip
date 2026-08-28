numero=8  #le pongo valor a numero
if numero == 0: #si compara si el numero es igual a 0, y si es asi imprime 0
    print ("0")

octal = "" #aqui se asigna un valor vacio a la variable octal
while numero > 0: #cuando el numero es mayor a 0 lo divide entre 8 y el residuo lo agrega a la variable octal, y el cociente lo asigna a numero.
    residuo = numero % 8
    octal = str(residuo) + octal
    numero = numero // 8
print (octal) 