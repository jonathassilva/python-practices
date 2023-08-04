def converter(bytes):
    div = 1024 * 1024
    return bytes / div

#main
arq = open("files/arquivo.txt")
linhas = arq.readlines()
tot = 0
cont = 0
for linha in linhas:
    valor = linha[15:]
    numeros = int(valor)
    mega = converter(numeros)
    tot += mega
    cont += 1
    print(f"{linha[0:15]} {mega:.2f} MB")

medio = tot / cont
print(f"Espaço total ocupado: {tot:.2f} MB")
print(f"Espaço médio ocupado: {medio:.2f} MB")
