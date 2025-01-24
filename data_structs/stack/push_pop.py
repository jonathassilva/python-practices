def cria_nodo(valor):
    """Cria um novo nó contendo o valor a ser inserido na pilha."""
    nodo = dict()
    nodo['valor'] = valor
    nodo['prox'] = None
    return nodo

def cria_pilha():
    """Cria uma pilha inicialmente vazia."""
    pilha = dict()
    pilha['topo'] = None
    pilha['tamanho'] = 0
    return pilha

def push(pilha, valor):
    """Cria um nó contendo o valor especificado pelo parâmetro e o insere no topo da pilha."""
    novo = cria_nodo(valor)
    novo['prox'] = pilha['topo']
    pilha['topo'] = novo
    pilha['tamanho'] += 1
    print(f"push {valor}")

def pop(pilha):
    """Remove um nó do topo da pilha e retorna seu valor."""
    if pilha['tamanho'] == 0:
        return None  # Pilha vazia
    topo = pilha['topo']
    pilha['topo'] = topo['prox']
    pilha['tamanho'] -= 1
    print(f"pop {topo['valor']}")
    return topo['valor']

def peek(pilha):
    """Retorna o valor guardado no nó que está no topo da pilha sem modificar a pilha."""
    if pilha['topo'] is None:
        return None
    return pilha['topo']['valor']

def tamanho(pilha):
    """Retorna o número de elementos da pilha."""
    return pilha['tamanho']

def processa_sequencia():
    """Processa números inteiros lidos até que o topo da pilha contenha o valor zero ou as operações não possam continuar."""
    pilha = cria_pilha()

    while True:
        numero = int(input("Digite um número inteiro: "))
        push(pilha, numero)

        while True:
            topo = peek(pilha)
            if topo is None or topo == 0 or tamanho(pilha) < 2:
                return

            if topo < 0:
                # Tenta desempilhar dois elementos e somá-los
                primeiro = pop(pilha)
                segundo = pop(pilha)
                soma = primeiro + segundo
                push(pilha, soma)
            else:
                break

# Iniciar o processamento
def main():
    print("Digite números inteiros para empilhar. O programa parará se o topo da pilha for 0 ou as operações não puderem continuar.")
    processa_sequencia()

if __name__ == "__main__":
    main()
