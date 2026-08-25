n=int(input("introduce un numero: "))
if n <= 1:
    print("no es primo")
i=2
while i <= n : 
    if n ==2:
        print("es primo")
        break
    if n % i == 0 and i != 2:
        print("no es primo")
        break
    elif n % i == 0 and i == n:
        print("primo")
        break
    elif n % i !=0 and i < n:
        print("es primo")
        break
    i=i+1 
    

   

