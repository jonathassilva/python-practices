penultimo = 0
ultimo = 1

numero = int(input("Digite o valor limite"))

if (numero == 1):
    print(penultimo)
elif (numero == 2):
    print(penultimo, ultimo, sep=",", end=" ")
else:
    print(penultimo, ultimo, sep=",", end=" ")
    for i in range (3, numero):
        atual = penultimo + ultimo
        print(",", atual, end=" ")
        penultimo = ultimo
        ultimo = atual