print("Dame el valor de la constante a")
a = float(input())
print("Give me the value for the constant b")
b = float(input())
print("Dammi il valore della costante c")
c = float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    print("Raices reales")
    x1 = -b + sqrt(d) / 2 * a
    x1i = 0.0
    x2 = -b - sqrt(d) / 2 * a
    x2i = 0.0
else:
    print("Raices imagiarias")
    x1 = -b / 2 * a
    x1i = sqrt(fabs(d)) / 2 * a
    x2 = x1
    x2i = -1 * x1i
print("x" + str(x1) + "" + str(x1i) + "i")
print("x2" + str(x2) + "" + str(x2i) + "i")
