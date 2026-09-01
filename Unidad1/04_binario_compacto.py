numero, binario= 8,"" #aqui se asigna el valor 8 a la variable numero y un valorvacio a la variable binario
if numero == 0:print ("0") #compara si el numero es igual a 0, y si es asi imprime 0
while numero > 0: binario,numero = str(numero % 2) + binario, numero // 2 #cuando el numero es mayor a 0 lo divide entre 2 y el residuo lo agrega a la variable binario, y el cociente lo asigna a numero. 
print (binario) #imprime el nuevo valor de binario.

 