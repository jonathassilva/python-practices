def insertion_sort(values:list) -> list:
    size = len(values)
    swap = False
    for i in range(size - 1):
        element = values[i+1]
        j = i
        while j >= 0 and element < values[j]:
            swap = True
            values[j+1] = values[j]
            j = j - 1
        
        if swap:
            values[j+1] = element
            swap = False
    return values

def clean_input(data:str) -> list:
    values = []
    for c in raw_data:
        if c.isnumeric():
            values.append(int(c))
    
    return values


raw_data = input()
values = clean_input(raw_data)

print(values)
sorted_values = insertion_sort(values)
print(sorted_values)