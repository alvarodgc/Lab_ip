print("Cuantas veces?  ")
x = int(input())
x = x - 1
print("Cuando termina?  ")
i = int(input())
while True:    #This simulates a Do Loop
    print("Hola mundo cruel" + str(x + 1))
    x = x + 1
    if x >= i: break
