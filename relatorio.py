from typing import TextIO


def gera_Relatorio(file: TextIO, dados: list,
                   pos: int, tamanho_total: float) -> None:
    per = 100 * (float(dados[1]) / tamanho_total)
    t = len(dados[0])
    nome = f"{pos}    " + dados[0] + (' ' * (15 - t))
    mem = float(dados[1]) / (1024 ** 2)
    string = f"{nome}"
    string += f" {mem:1.2f} MB"
    string += "             " + f"{per:1.2f}\n"
    file.write(string)


with open("usuarios.txt", encoding='utf-8') as file:
    i = 0
    tamanhoT = 0
    with open('relatorio.txt', "w", encoding='utf-8') as dest:
        dest.write("ACME Inc.               Uso do espaço" +
                   "em disco pelos usuários\n" +
                   "-------------------------------------" +
                   "-----------------------------------\n" +
                   "Nr.  Usuário        Espaço utilizado     % do uso\n\n")

        for line in file:
            data = line.split()
            tamanhoT += float(data[1])
            i += 1
            gera_Relatorio(dest, data, i, tamanhoT)

        dest.write(f"Espaço total ocupado: {tamanhoT/(1024 ** 2):.2f} MB\n"
                   + "Espaço médio ocupado: "
                   + f"{tamanhoT/((1024 ** 2)*i):.2f} MB")
