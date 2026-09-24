print("inicio del ciclo exterior:  ")
iniciocicloexterior = int(input())
print("Dame el fin del ciclo exterior : ")
fincicloexterior = int(input())
print("Dame el inicio del ciclo interior : ")
iniciociclointerior = int(input())
print("Dame el fin del ciclo interior : ")
finciclointerior = int(input())
i = iniciocicloexterior
while i <= fincicloexterior:
    print("Tabla = " + str(i))
    j = iniciociclointerior
    while j <= finciclointerior:
        print(str(i) + " * " + str(j) + "=" + str(i * j))
        j = j + 1
    i = i + 1