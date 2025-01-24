def cria_programa(nome, tempo_restante):
    """Cria um dicionário que representa um nó da lista duplamente encadeada, inicialmente
    apontando para None. Você deve ajustar as referências para inserir este nó na lista.
    """
    programa = dict()
    programa['nome'] = nome
    programa['tempo_restante'] = tempo_restante
    programa['ant'] = None
    programa['prox'] = None
    return programa

def cria_lista():
    """Cria um dicionário que representa uma lista circular inicialmente vazia.
    """
    lista = dict()
    lista['prim'] = None
    lista['num_programas'] = 0
    return lista

def insere_fim(lista, programa):
    """Insere um nó (programa) no fim da lista. O parâmetro programa é uma
    referência para um nó criado pela função cria_programa().
    """
    if lista['prim'] is None:
        lista['prim'] = programa
        programa['prox'] = programa
        programa['ant'] = programa
    else:
        ultimo = lista['prim']['ant']
        ultimo['prox'] = programa
        programa['ant'] = ultimo
        programa['prox'] = lista['prim']
        lista['prim']['ant'] = programa
    lista['num_programas'] += 1

def remove(lista, programa):
    """Remove um programa (nó) da lista encadeada.
    """
    if lista['num_programas'] == 1:
        lista['prim'] = None
    else:
        programa['ant']['prox'] = programa['prox']
        programa['prox']['ant'] = programa['ant']
        if lista['prim'] == programa:
            lista['prim'] = programa['prox']
    lista['num_programas'] -= 1

# Lê as configurações do exercício
cota, num_programas = map(int, input().split(' '))

# Cria uma lista ligada vazia
lista = cria_lista()

# Lê os programas e os insere na lista
for _ in range(num_programas):
    nome, tempo_total_string = input().split(' ')
    programa = cria_programa(nome, int(tempo_total_string))
    insere_fim(lista, programa)

# Simulação do sistema de tempo compartilhado
tempo_atual = 0
while lista['num_programas'] > 0:
    programa_atual = lista['prim']
    if programa_atual['tempo_restante'] <= cota:
        tempo_atual += programa_atual['tempo_restante']
        print(f"{tempo_atual} us: {programa_atual['nome']} finalizou")
        remove(lista, programa_atual)
    else:
        tempo_atual += cota
        programa_atual['tempo_restante'] -= cota
    lista['prim'] = programa_atual['prox']

print(f"{tempo_atual} us: shutdown")
