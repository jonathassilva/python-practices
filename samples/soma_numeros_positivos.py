maior = 0
cont = 0

for cont in range(1, 6):
    numero = int(input("Digite o {} numero: ".format(cont)))
    while(numero <=0):
        print("Erro! Digite um numero positivo")
        numero = int(input("Digite um numero: "))

    if (numero > maior):
        maior = numero

print("O maior numero é: ", maior)