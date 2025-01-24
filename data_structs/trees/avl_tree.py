def clean_input(data: str) -> list:
    values = []
    if data != '[]':
        data = data.strip("[]").split(",")
        values = [int(number.strip()) for number in data]
    return values

def height(T: dict) -> int:
    return T['h'] if T else 0

def balance_factor(T: dict) -> int:
    return height(T['right']) - height(T['left']) if T else 0

def update_height(T: dict):
    if T:
        T['h'] = 1 + max(height(T['left']), height(T['right']))

def rotation_ll(T: dict) -> dict:
    if not T or not T['left']:
        return T

    aux = T['left']
    T['left'] = aux['right']
    aux['right'] = T

    update_height(T)
    update_height(aux)

    return aux

def rotation_rr(T: dict) -> dict:
    if not T or not T['right']:
        return T

    aux = T['right']
    T['right'] = aux['left']
    aux['left'] = T

    update_height(T)
    update_height(aux)

    return aux

def rotation_lr(T: dict) -> dict:
    if T and T['left']:
        T['left'] = rotation_rr(T['left'])
    return rotation_ll(T)

def rotation_rl(T: dict) -> dict:
    if T and T['right']:
        T['right'] = rotation_ll(T['right'])
    return rotation_rr(T)

def insert(T: dict, value: int) -> dict:
    if not T:
        T = {
            'value': value,
            'left': None,
            'right': None,
            'h': 1
        }
    elif value < T['value']:
        T['left'] = insert(T['left'], value)
    else:
        T['right'] = insert(T['right'], value)

    update_height(T)

    # Perform balancing if needed
    bf = balance_factor(T)

    if bf < -1:  # Left heavy
        if value < T['left']['value']:  # Left-Left case
            return rotation_ll(T)
        else:  # Left-Right case
            return rotation_lr(T)
    elif bf > 1:  # Right heavy
        if value > T['right']['value']:  # Right-Right case
            return rotation_rr(T)
        else:  # Right-Left case
            return rotation_rl(T)

    return T

def pre_order(T: dict, result: list):
    if T:
        result.append(T['value'])
        pre_order(T['left'], result)
        pre_order(T['right'], result)

def pos_order(T: dict, result: list):
    if T:
        pos_order(T['left'], result)
        pos_order(T['right'], result)
        result.append(T['value'])

def format_output(tree_number: int, T: dict):
    pre_order_result = []
    pos_order_result = []
    pre_order(T, pre_order_result)
    pos_order(T, pos_order_result)

    print(f'Arvore {tree_number}')
    print(f'pre: {" ".join(map(str, pre_order_result))}')
    print(f'pos: {" ".join(map(str, pos_order_result))}')
    print()

def main():
    tree_number = 1

    while True:
        raw_data = input()
        values = clean_input(raw_data)

        if not values:
            break

        T = None
        for value in values:
            T = insert(T, value)

        format_output(tree_number, T)
        tree_number += 1

if __name__ == "__main__":
    main()
