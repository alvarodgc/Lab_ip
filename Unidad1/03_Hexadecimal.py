numero=16  #le pongo valor a numero
if numero == 0: #si numero es igual a 0 imprime 0, lo compara gracias al ==
    print ("0")

hexadecimal = ""# ponemos un valor vacio
while numero > 0:#mientras numero sea mayor a 0 se ejecuta:
    residuo = numero % 16 # calcula el residuo de numero entre 16
    if residuo < 10:print (residuo) # cuando el residuo es menor a 10 imprime el residuo
    if residuo == 10:print ("A") #si el residuo es igual a 10 imprime A
    if residuo == 11:print ("B") #si el residuo es igual a 11 imprime B
    if residuo == 12:print ("C") #igual a 12 imprime C
    if residuo == 13:print ("D") #igual a 13 imprime D
    if residuo == 14:print ("E") #igual a 14 imprime E
    if residuo == 15:print ("F") #igual a 15 imprime F
    hexadecimal = str(residuo) + hexadecimal #convierte el residuo en string y lo agrega a la variable hexadecimal
    numero = numero // 16 # divide el numero entre 16 y lo asigna a numero
print (hexadecimal) #imprime hexadecimal
