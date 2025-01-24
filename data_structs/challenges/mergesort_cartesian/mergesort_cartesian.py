class ponto:
    def __init__(self, x, y):
        """
        Construtor da classe ponto. Inicializa as coordenadas x e y e calcula a distância à origem.
        """
        self.x = x
        self.y = y
        self.distancia_origem = x ** 2 + y ** 2  # Armazena a distância quadrada para evitar uso de raiz quadrada

    def __lt__(self, outro):
        """
        Sobrecarga do operador < para comparação entre pontos.
        """
        # Critério 1: Menor distância à origem
        if self.distancia_origem != outro.distancia_origem:
            return self.distancia_origem < outro.distancia_origem
        # Critério 2: Coordenada x (mais à esquerda)
        if self.x != outro.x:
            return self.x < outro.x
        # Critério 3: Coordenada y (mais abaixo)
        return self.y < outro.y

def merge_sort(lista):
    """
    Implementação do algoritmo Merge Sort para ordenar uma lista.
    """
    if len(lista) > 1:
        meio = len(lista) // 2

        # Divisão da lista em duas metades
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Ordenação recursiva
        merge_sort(esquerda)
        merge_sort(direita)

        # Intercalação das duas metades
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes de cada metade
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# Leitura da entrada
entrada = eval(input())

# Cria uma lista de objetos da classe ponto
pontos = [ponto(x, y) for x, y in entrada]

# Ordena a lista de pontos usando Merge Sort
merge_sort(pontos)

# Imprime os pontos ordenados
for p in pontos:
    print(p.x, p.y)
