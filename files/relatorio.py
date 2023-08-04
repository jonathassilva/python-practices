nome_arquivo = 'nomes.txt'

def ler_arquivo(nome_arquivo):
    matriz = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Remova a quebra de linha (se houver) e divida a linha nos espaços em branco
            dados = linha.strip().split()
            # Certifique-se de que existam pelo menos 2 elementos em "dados"
            if len(dados) >= 2:
                matriz.append(dados[:2])  # Adiciona apenas os 2 primeiros elementos
    return matriz

matriz = ler_arquivo(nome_arquivo)
total = 0
for i in range(3):
    total += int(matriz[i][1])

def transformar_KBpraMB(kb):
    kilobytes = int(kb)
    return kilobytes / 1024 

def porcentagem_de_uso(porcentagem):
    return (porcentagem/total)*100

relatorio = [[0, 0, 0] for _ in range(3)]  # Inicializando a matriz relatorio com zeros

for i in range(3):
    relatorio[i][0] = matriz[i][0]  # Pegar os nomes
    relatorio[i][1] = transformar_KBpraMB(matriz[i][1])  # Pegando a segunda coluna que tem KB
    relatorio[i][2] = porcentagem_de_uso(int(matriz[i][1]))  # Pegar a porcentagem

# Exibindo o relatório
print("Nr.  Usuário        Espaço utilizado     Porcentagem do uso")
for i in range(3):
    print(f"{i+1}  {relatorio[i][0]:<15} {relatorio[i][1]:.2f} MB   {relatorio[i][2]:.2f}%")
