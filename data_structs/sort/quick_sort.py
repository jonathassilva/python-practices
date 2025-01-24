def partition(L:list) -> int:
    low = 0
    high = len(L) - 1
    pivot = L[(low + high) // 2]
    i = low - 1
    j = high + 1
    
    while True:
        while True:
            i += 1
            if L[i] >= pivot:
                break
        
        while True:
            j -= 1
            if L[j] <= pivot:
                break
        
        if i >= j:
            return j
        
        L[i], L[j] = L[j], L[i]

def quick_sort(L:list) -> list:
    if len(L) > 1:
        partition_index = partition(L)
        
        left_part = L[:partition_index + 1]
        right_part = L[partition_index + 1:]
        
        left_part = quick_sort(left_part)
        right_part = quick_sort(right_part)
        
        L[:len(left_part)] = left_part
        L[len(left_part):] = right_part
    return L

def clean_input(data: str) -> list:
    data = data.strip("[]").split(",")
    values = [int(numero.strip()) for numero in data]
    return values

raw_data = input()
values = clean_input(raw_data)
sorted_values = quick_sort(values)
print(sorted_values)