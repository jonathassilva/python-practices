import os

def bytes_to_mb(qtd_bytes):
    return str(round(qtd_bytes/1048576, 2)).replace('.', ',')

def percentual(tamanho_usado, total):
    return str(round(tamanho_usado*100/total,2)).replace('.',',')

if os.path.exists("usuarios.txt"):
    usuarios_tamanho_txt = open("usuarios.txt", "r")
    usuarios_tamanhos = usuarios_tamanho_txt.read().split("\n")

    arquivo_relatorio = open("relatório.txt", "wt")
    arquivo_relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários")
    arquivo_relatorio.write("-"*72 + "\n")

    arquivo_relatorio.write("Nr.".ljust(5))
    arquivo_relatorio.write("Usuário".ljust(15))
    arquivo_relatorio.write("Espaço utilizado".ljust(21))
    arquivo_relatorio.write("'%' do uso".ljust(9)+ "\n\n")

    espaco_total = 0

    for usuario_tamanho in usuarios_tamanhos:
        espaco_total += int(usuario_tamanho.split()[1])
    for indice_usuario_tamanho in range (len(usuarios_tamanhos)):
        usuario_tamanho = usuarios_tamanhos[indice_usuario_tamanho].split()

        usuario = usuario_tamanho[0]
        tamanho = usuario_tamanho[1]

        arquivo_relatorio.write(str(indice_usuario_tamanho+1).ljust(5))
        arquivo_relatorio.write(usuario.ljust(15))
        arquivo_relatorio.write(bytes_to_mb(int(tamanho)).rjust(7)+" MB             ")
        arquivo_relatorio.write(percentual(int(tamanho), espaco_total).rjust(7)+"%\n")
    arquivo_relatorio.write("\nEspaço total ocupado: " + bytes_to_mb(espaco_total) + "MB\n")
    arquivo_relatorio.write("Espaço médio ocupado: " + bytes_to_mb(espaco_total/len(usuarios_tamanhos)) + "MB")
                            

else:
    print("Arquivo não encontrado!")