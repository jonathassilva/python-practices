pecas = 0
tempo = 0

soma_quantidade_pecas = 0
soma_tempo = 0
maior_quantidade_pecas = 0
tempo_maior_quantidade_pecas = 0
quantidade_medicoes = 0


pecas = int(input("Peças? "))
tempo = int(input("Tempo? "))

while tempo > 0:
    soma_quantidade_pecas = soma_quantidade_pecas + pecas
    soma_tempo = soma_tempo + tempo
    if pecas > maior_quantidade_pecas:
        maior_quantidade_pecas = pecas
        tempo_maior_quantidade_pecas = tempo
    quantidade_medicoes = quantidade_medicoes + 1
    pecas = int(input("Peças?"))
    tempo = int(input("Tempo? "))
    

media_pecas = soma_quantidade_pecas / soma_tempo
print("Média de peças por tempo: ", round(media_pecas, 2))
print("Maior quantidade pro funcionario: ", maior_quantidade_pecas, "Tempo: ", tempo_maior_quantidade_pecas)
print("Total de Peças: ", soma_quantidade_pecas)
print("Medições: ", quantidade_medicoes)