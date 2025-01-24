def brincadeira_com_cartas():
    while True:
        # Ler a entrada
        entrada = input().strip()
        
        # Converte para uma lista de números inteiros
        numeros = list(map(int, entrada.split()))

        for n in numeros:
            if n == 0:
                return

            # Criando a lista ligada com dicionários
            monte = {i: i + 1 for i in range(1, n)}
            monte[n] = None  # Último elemento aponta para None

            primeiro = 1  # Referência para o primeiro elemento
            ultimo = n  # Referência para o último elemento

            descartadas = []

            # Simulação da brincadeira
            while monte[primeiro] is not None:
                descartadas.append(primeiro)  # Adiciona o primeiro à lista de descartadas
                primeiro = monte[primeiro]  # Atualiza o primeiro para o próximo
                
                # Move o próximo para o final da fila
                monte[ultimo] = primeiro
                ultimo = primeiro
                primeiro = monte[primeiro]
                monte[ultimo] = None

            # Última carta restante
            restante = primeiro

            # Imprimir os resultados
            print("Descartadas:", " ".join(map(str, descartadas)))
            print("Restou:", restante)

            print()  # Linha em branco entre as partidas

brincadeira_com_cartas()