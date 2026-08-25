numero, octal=8,""
if numero == 0:print ("0") #compara si el numero es igual a 0, y si es asi imprime 0
while numero > 0: binario,numero = str(numero % 2) + octal, numero/ 2 #cuando el numero es mayor a 0 
print (binario) #imprime el nuevo valor de binario.
