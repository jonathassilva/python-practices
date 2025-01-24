def selection_sort(values: list) -> list:
    size = len(values)
    for i in range(size):
        minor_index = i
        for j in range(i, size):
            if values[j] < values[i]:
                minor_index = j
        if minor_index != i:
            print(values[i], '<->', values[minor_index])
            aux = values[i]
            values[i] = values[minor_index]
            values[minor_index] = aux
        
    return values

def clean_input(data: str) -> list:
    values = []
    for c in data:
        if c.isnumeric():
            values.append(int(c))
    return values

raw_data = input()
values = clean_input(raw_data)
sorted_values = selection_sort(values)
print(sorted_values)