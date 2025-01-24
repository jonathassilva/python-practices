def max_heapify(arr, i, n):
    max_value = i  # Inicializa o max_value como o índice atual
    left = 2 * i + 1  # Índice do filho esquerdo
    right = 2 * i + 2  # Índice do filho direito

    # Verifica se o filho esquerdo é max_value que o elemento atual
    if left < n and arr[left] > arr[max_value]:
        max_value = left

    # Verifica se o filho direito é max_value que o elemento atual
    if right < n and arr[right] > arr[max_value]:
        max_value = right

    # Se o max_value não for o elemento atual, troca os elementos e chama recursivamente
    if max_value != i:
        arr[i], arr[max_value] = arr[max_value], arr[i]
        max_heapify(arr, max_value, n)


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
    max_heapify(lista, 0, n)
    print(lista)

