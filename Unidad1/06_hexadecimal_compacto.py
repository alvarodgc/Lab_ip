numero , hexadecimal=15 , ""
if numero == 0:  print ("0")
while numero > 0:
    residuo = numero % 16
    if residuo < 10:print (residuo)
    if residuo == 10:print ("A")
    if residuo == 11:print ("B")
    if residuo == 12:print ("C")
    if residuo == 13:print ("D")
    if residuo == 14:print ("E")
    if residuo == 15:print ("F")
    hexadecimal = str(residuo) + hexadecimal
    numero = numero // 16 
    print (hexadecimal)
