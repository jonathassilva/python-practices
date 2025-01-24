def merge_sort(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left_half = L[:mid]
    right_half = L[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def clean_input(data: str) -> list:
    data = data.strip("[]").split(",")
    values = [int(numero.strip()) for numero in data]
    return values

while True:
    raw_data = input()
    if raw_data.strip() == "[]":
        break

    values = clean_input(raw_data)

    sorted_list = merge_sort(values)
    print(sorted_list)