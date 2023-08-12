from typing import TextIO

# Aluno: Carlos Eduardo


def gera_Relatorio(file: TextIO, users: list,
                   memory: int, total: float) -> None:
    for i in range(0, len(users)):
        espacoMB = memory[i] / (1024.0 * 1024.0)
        percentUse = memory[i] / total
        file.write(f'\n{i + 1}    {users[i]:<15}{espacoMB:>7.2f}'
                   + f' MB{percentUse * 100.0:>18.2f}%')

    file.write('\n\nEspaco total ocupado: %.2f MB' %
               (total / (1024.0 * 1024.0)))
    file.write('\nEspaco medio ocupado: %.2f MB' %
               (total / len(users) / (1024.0 * 1024.0)))


with open("usuarios.txt", encoding='utf-8') as file:

    lines = file.readlines()
    users = []
    memory = []
    total = 0
    for x in lines:
        line = x.split()
        users.append(line[0])
        memory.append(int(line[1]))
    total = sum(memory)

    arquivoRelatorio = open('relatorio.txt', 'w')
    arquivoRelatorio.write(
        'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
    arquivoRelatorio.write(72 * '-')
    arquivoRelatorio.write(
        '\nNr.  Usuario        Espaco utilizado     %% do uso')
    gera_Relatorio(arquivoRelatorio, users, memory, total)

    arquivoRelatorio.close()
