import os

def bytes_to_mb(qtd_bytes):
    return str(round(qtd_bytes/1048576, 2)).replace('.', ',')

def percentual(tamanho_usado, total):
    return str(round(tamanho_usado*100/total,2)).replace('.',',')

if os.path.exists("usuarios.txt"):
    usuarios_tamanho_txt = open("usuarios.txt", "r")
    usuarios_tamanho = usuarios_tamanho_txt.read().split("\n")

    arquivo_relatorio = open("relatório.txt", "wt")
    arquivo_relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários")
    arquivo_relatorio.write("-"*72 + "\n")
    

else:
    print("Arquivo não encontrado!")