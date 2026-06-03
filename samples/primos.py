numero = int(input("Digite um numero: "))
achou = False

if (numero == 1 or numero == 2):
    print("Numero não é primo")

else:
    for i in range(2, numero):
        if numero % i == 0:
            achou = True
            break

if (achou):
    print("Numero não é primo")
else:
    print("Numero primo")    
