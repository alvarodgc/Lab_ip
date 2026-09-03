numero , hexadecimal=17, ""  # aqui le puse valores a numero y hexadecimal 
if numero == 0:  print ("0")  # aqui compara si el numero es igual a 0 y sisi imprime el 0 en la variable vacia
while numero > 0:  #aqui puse un bucle, mientras el numerp sea mayor a 0 se ejecuta.
    residuo = numero % 16   #aqui calcula el residuo de numero entre 16
    if residuo == 10:residuo = "A"  # aqui compara si el residuo es igual a 10 y si es asi le asigna A a la variable residuo
    if residuo == 11:residuo = "B"   #igual que el anterior pero con B
    if residuo == 12:residuo = "C"   #igual 
    if residuo == 13:residuo = "D"   #igual 
    if residuo == 14:residuo = "E"   #igual 
    if residuo == 15:residuo = "F"   #igual 
    hexadecimal = str(residuo) + hexadecimal  #aqui convierte el residuo en string y lo agrega a la variable hexadecimal
    numero = numero // 16  #aqui divide el numero entre 16 y lo asigna a numero
    print (hexadecimal)    #impime la variable hexadecimal
   