maior = 0
cont = 0
'''
Repetição usando o while
'''
# while (cont < 5):
#     numero = int(input("Digite um numero: "))
#     if (numero > maior):
#         maior = numero
#     cont = cont + 1

'''
Repetição usando o for
'''
for cont in range(1, 6):
    numero = int(input("Digite um numero: "))
    if (numero > maior):
        maior = numero
print("O maior numero é: ", maior)