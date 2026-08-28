numero=8 #aqui se asigna el valor 8 a la variable numero
if numero == 0: #compara si el numero es igual a 0, y si es asi imprime 0
    print ("0") #imprime el 0
binario = "" # aqui se asigna un valor vacio a la variable binario
while numero > 0: #cuando el numero es mayor a 0 lo divide entre 2 y el residuo lo agrega a la variable binario, y el cociente lo asigna a numero.
    residuo = numero % 2
    binario = str(residuo) + binario
    numero = numero // 2
print (binario) #imprime el nuevo valor de binario.
