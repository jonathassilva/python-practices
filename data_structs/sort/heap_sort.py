def max_heapify(values, i, n):
    """
    Função que corrige uma "quase-heap" máxima a partir do índice i.
    :param values: Lista representando a "quase-heap".
    :param i: Índice do elemento a ser verificado.
    :param n: Tamanho atual da heap.
    """
    max_value = i  # Inicializa o max_value como o índice atual
    left = 2 * i + 1  # Índice do filho esquerdo
    right = 2 * i + 2  # Índice do filho direito

    # Verifica se o filho esquerdo é max_value que o elemento atual
    if left < n and values[left] > values[max_value]:
        max_value = left

    # Verifica se o filho direito é max_value que o elemento atual
    if right < n and values[right] > values[max_value]:
        max_value = right

    # Se o max_value não for o elemento atual, troca os elementos e chama recursivamente
    if max_value != i:
        values[i], values[max_value] = values[max_value], values[i]
        max_heapify(values, max_value, n)


def build_max_heap(values):
    """
    Transforma uma lista em uma heap máxima.
    :param values: Lista a ser transformada em heap.
    """
    n = len(values)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(values, i, n)


def heap_sort(values):
    """
    Ordena uma lista usando o algoritmo Heap Sort.
    :param values: Lista a ser ordenada.
    """
    n = len(values)
    build_max_heap(values)  # Constrói a heap máxima

    # Realiza o processo de ordenação
    for i in range(n - 1, 0, -1):
        values[0], values[i] = values[i], values[0]  # Troca o max_value elemento com o último
        max_heapify(values, 0, i)  # Corrige a heap sem o último elemento


def clean_input(data: str) -> list:
    data = data.strip("[]").split(",")
    values = [int(numero.strip()) for numero in data]
    return values

while True:
    raw_data = input()
    if raw_data.strip() == "[]":
        break

    lista = clean_input(raw_data)

    n = len(lista)
    heap_sort(lista)
    print(lista)

