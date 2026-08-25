n=input("introduce un numero: ")
i=2
n=int(n)
while i*i<=n:
    if n%i==0:
        print("primo")
        break
    else:
        print("no primo")
        break    
    i=i+1    
    