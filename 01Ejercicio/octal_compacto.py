numero, octal=8,"" #aqui se asigna el valor 8 a la variable numero y un valor vacio a la variable octal
if numero == 0:print ("0") #compara si el numero es igual a 0, y si es asi imprime 0
while numero >0: octal,numero = str(numero % 8) + octal, numero // 8  #cuando el numero es mayor a 0 lo divide entre 8 y el residuo lo agrega a la variable octal, y el cociente lo asigna a numero.
print (octal) #imprime el nuevo valor de octal.
