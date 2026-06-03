numero = int(input("Digite um numero: "))

for i in range(3, numero +1):
    achou = False
    for j in range(2, i):
        if i % j == 0:
            achou = True
    
    if (not achou):
        print(i, end=" ")
 
