def get_dicioU (arquivo):
    espaçoU = {}
    for linha in arquivo:
        usuario, espaço = linha.split()
        espaçoU[usuario] = espaço
    arquivo.close()
    return espaçoU

def get_total (espaçoU):
    espaçoT = 0
    for usuario in espaçoU:
        espaçoT += int(espaçoU[usuario])
    return espaçoT

def conversor_de_bytes (tamanho, grauConversao, invertido=False):
    if not invertido:
        tamanhoNovo = tamanho/1024**grauConversao
    else:
        tamanhoNovo = tamanho*1024**grauConversao
    return(tamanhoNovo)

def get_percentual_de_uso (espaço, espaçoT):
    percentual = espaço/espaçoT*100
    return percentual

espaçoU = get_dicioU(open("files/usuarios.txt", "r"))
espaçoT = get_total(espaçoU)

print("ACME Inc.               Uso do espaço em disco pelos usuários\n" + 
      "------------------------------------------------------------------------\n" +
      "Nr.  Usuário        Espaço utilizado     % do uso")
cont = 1
for usuario in espaçoU:
    espaço_bytes = round(conversor_de_bytes(int(espaçoU[usuario]), 2), 2)
    percentual_de_uso = round(get_percentual_de_uso(int(espaçoU[usuario]), espaçoT), 2)
    print("{}    {}{} MB{}{}%".format(cont, usuario + " "*int(15-len(usuario)), espaço_bytes, " "*int((18-len(str(espaço_bytes)))), percentual_de_uso))