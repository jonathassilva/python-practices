def create_linked_list():
    linked_list = dict()
    linked_list['first'] = None
    linked_list['size'] = 0

    return linked_list

def linked_list_print(linked_list):
    if linked_list['first'] is None:
        print('prim --> ||-', end='\n\n')
    else:
        print('prim -->', end=' ')
        point = linked_list['first']
        print(point['value'], end=' -> ')
        while point['next'] is not None:
            point = point['next']
            print(point['value'], end=' -> ')
        print('||-', end='\n\n')

def linked_list_insert_first(linked_list, value):
    """ Add a int value in linked_list begin"""
    novo = dict()
    novo['next'] = None
    novo['value'] = value
    
    if linked_list['first'] is None:
        linked_list['first'] = novo
    else:
        novo['next'] = linked_list['first']
        linked_list['first'] = novo
    
    linked_list['size'] += 1

    return linked_list

def linked_list_insert_last(linked_list, value):
    """ Insere um valor inteiro no fim de uma linked_list passada por parametro"""
    novo = dict()
    novo['next'] = None
    novo['value'] = value

    # Create a pointer for fisrt element
    point = linked_list['first']

    if linked_list['first'] is None:
        linked_list['first'] = novo
    else:
        # Search for the last element
        while point['next'] is not None:
            point = point['next']
        
        point['next'] = novo

    linked_list['size'] += 1

    return linked_list

def linked_list_insert_by_index(linked_list, value, index):
    """ Insere um valor inteiro no fim de uma linked_list passada por parametro"""
    new = dict()
    new['next'] = None
    new['value'] = value

    if linked_list['first'] is None:
        print('Lista vazia!')
        print('Inserindo no inicio da lista...')
        linked_list_insert_first(linked_list, value)
    elif index > linked_list['size']:
        print('Posição maior que a lista!')
        print('Inserindo no fim da lista...')
        linked_list_insert_last(linked_list, value)
    else:
        pos_aux = 1
        pointer = linked_list['first']

        # Enquanto a proxima posição nao for a de inserir
        while index != pos_aux + 1:
            pos_aux+=1
            pointer = pointer['next']
        
        new['next'] = pointer['next']
        pointer['next'] = new
    
    
    linked_list['size'] += 1

    return linked_list

def linked_list_remove_first(linked_list):
    if linked_list['first'] is None:
        print('Lista já vazia')
    elif linked_list['size'] == 1:
        linked_list['size'] -= 1
        temp = linked_list['first']
        linked_list['first'] = None
        temp = None
    else:
        linked_list['size'] -= 1
        temp = linked_list['first']
        linked_list['first'] = temp['next']
        temp = None

    return linked_list
        
def linked_list_remove_by_index(linked_list, index):
    if linked_list['first'] is None:
        print('Lista já vazia')
    elif pos > linked_list['size']:
        print('Indice invalido!')
    elif pos == 1:
        linked_list = linked_list_remove_first(linked_list)
    else:
        pos_aux = 1
        pointer = linked_list['first']

        # Enquanto a proxima posição nao for a de remover
        while index != pos_aux + 1:
            pos_aux+=1
            pointer = pointer['next']
        
        temp = pointer['next']
        pointer['next'] = temp['next']
        temp = None

        linked_list['size'] -= 1
    
    return linked_list

def linked_list_remove_by_value(linked_list, value):
    if linked_list['first'] is None:
        print('Lista já vazia')
    elif linked_list['first']['value'] == value:
        temp = linked_list['first']
        linked_list = temp['next']
        temp = None
        linked_list['size'] -= 1
    else:
        pointer = linked_list['first']
        # Enquanto a proxima posição nao for a de remover
        while pointer['next']['value'] != value:
            pointer = pointer['next']        
        temp = pointer['next']
        pointer['next'] = temp['next']
        temp = None

        linked_list['size'] -= 1
    
    return linked_list

def linked_list_destroy(linked_list):
    if linked_list['first'] is None:
        print('Lista vazia. Destruindo a lista...')
    else:
        while linked_list['first'] is not None:
            linked_list = linked_list_remove_first(linked_list)
    
    linked_list = None
    return linked_list


print('### AED - LISTAS ENCADEADAS ###')
linked_list = create_linked_list()
print('linked_list criada com sucesso!', end='\n\n')

while True:
    print('1 - Mostrar uma linked_list;')
    print('2 - Inserir um valor no início da linked_list')
    print('3 - Inserir um valor no fim da linked_list')
    print('4 - Inserir um valor em uma posicao da linked_list')
    print('5 - Remoção no inicio da lista')
    print('6 - Remover uma posicao especifica da linked_list')
    print('7 - Remover um valor especific da linked_list')
    print('8 - Destruir')
    print('9 - Encerrar', end='\n')
 
    opcao = int(input('Escolha uma opção para realizar: '))
    match opcao:
        case 1:
            linked_list_print(linked_list)
        
        case 2:
            value = int(input('Inserir o valor: '))
            linked_list = linked_list_insert_first(linked_list, value)
            linked_list_print(linked_list)

        case 3:
            value = int(input('Inserir o valor: '))
            linked_list = linked_list_insert_last(linked_list, value)
            linked_list_print(linked_list)
        
        case 4: 
            value = int(input('Inserir o valor: '))
            pos = int(input('Inserir na posição ?: '))
            linked_list = linked_list_insert_by_index(linked_list, value, pos)
            linked_list_print(linked_list)

        case 5: 
            linked_list = linked_list_remove_first(linked_list)
            linked_list_print(linked_list)

        case 6:
            pos = int(input('Remover na posição ?: '))
            linked_list = linked_list_remove_by_index(linked_list, pos)
            linked_list_print(linked_list)

        case 7:
            value = int(input('Qual valor quer remover?: '))
            linked_list = linked_list_remove_by_value(linked_list, value)
            linked_list_print(linked_list)
        
        case 8:
            linked_list = linked_list_destroy(linked_list)
            print('Lista destruída. Encerrando o programa...')
            break

        case 9:
            print('Encerrando o programa...')
            break 
        case _:
            print("Opção inválida.")