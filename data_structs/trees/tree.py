def insert(T, value):
    if T is None:
        T = dict()
        T['value'] = value
        T['left'] = None
        T['right'] = None
    elif value > T['value']:
        T['right'] = insert(T['right'], value)
    else:
        T['left'] = insert(T['left'], value)
    
    return T

def search(T, value):

    if T == None:
        return None
    
    if T['value'] == value:
        return T
    
    if value > T['value']:
        return search(T['right'], value)        
    
    else:
        return search(T['left'], value)

def print_pre_order(T):
    if T is not None:
        # Visita a raiz
        print(T['value'], end=' ')

        # Percorre a subarvore a esquerda em pre-ordem
        print_pre_order(T['left'])

        # Percorre a subarvore a esquerda em pre-ordem
        print_pre_order(T['right'])

def print_pos_order(T):
    if T is not None:

        # Percorre a subarvore a esquerda em pre-ordem
        print_pos_order(T['left'])

        # Percorre a subarvore a direita em pre-ordem
        print_pos_order(T['right'])

        # Visita a raiz
        print(T['value'], end=' ')
  
def print_in_order(T):
    if T is not None:

        # Percorre a subarvore a esquerda em pre-ordem
        print_in_order(T['left'])

        # Visita a raiz
        print(T['value'], end=' ')

        # Percorre a subarvore a direita em pre-ordem
        print_in_order(T['right'])


def find_min_bst(T):
    if T is None:
        pass
    if T['left'] is None:
        return T
    return find_min_bst(T['left'])

def find_max_bst(T):
    if T is None:
        pass
    if T['right'] is None:
        return T
    return find_max_bst(T['right'])

root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


print_pre_order(root)
print()
print_pos_order(root)
print()
print_in_order(root)

print(find_min_bst(root))
print(find_max_bst(root))