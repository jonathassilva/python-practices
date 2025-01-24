'''
Trocas do Bubble Sort

Implementação do algoritmo BubbleSort, que recebe uma lista por parâmetro,
e além de retornar a lista ordenada, ainda apresenta as trocas realizadas.

Exemplo 1

Entrada:

[1,3,2,4,5,8,6,7]

Saída esperada:

3 <-> 2
8 <-> 6
8 <-> 7
[1, 2, 3, 4, 5, 6, 7, 8]


Exemplo 2:

Entrada:

[1,2,3,6,5,4]

Saída esperada:

6 <-> 5
6 <-> 4
5 <-> 4
'''

def bubble_sort(values: list) -> list:
    for j in range(len(values) - 1, 0, -1):
        for i in range(j):
            if values[i] > values[i + 1]:
                print(values[i], '<->', values[i + 1])
                aux = values[i]
                values[i] = values[i+1]
                values[i+1] = aux
    return values

def clean_input(data: str) -> list:
    values = []
    for c in raw_data:
        if c.isnumeric():
            values.append(int(c))
    return values

raw_data = input()
values = clean_input(raw_data)
sorted_values = bubble_sort(values)
print(sorted_values)
