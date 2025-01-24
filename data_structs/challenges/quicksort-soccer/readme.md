### O Quick Sort no Brasileirão

Futebol é o esporte mais popular do planeta, contando com milhares de times em campeonatos ao redor do mundo inteiro.

Com tantos times, é dura a tarefa manter registro dos jogos e dos placares de todos os campeonatos. Portanto, neste exercício você deve escrever um programa que recebe o nome de um campeonato, os nomes dos times e uma descrição de todos os jogos. Calcule e imprima a tabela do campeonato, em ordem do vencedor ao perdedor.

Cada jogo pode terminar em vitória de um dos times ou empate. Não há diferença entre jogos em casa ou como visitante. O time vencedor leva 3 pontos e, em caso de empate, ambos os times levam 1 ponto.

O placar geral do campeonato deve ser ordenado, com o método Quick Sort, pelos seguintes critérios:

- O primeiro critério é o número de pontos. Um time que fez mais pontos, obviamente, estará melhor classificado que os times com menor número de pontos;
- O segundo critério é o número de vitórias. Se dois times tiverem o mesmo número de pontos, então o time que tiver mais vitórias estará melhor classificado;
- O terceiro critério é o saldo de gols. Se dois times empatarem nos critérios anteriores, então o time que tiver a maior diferença entre gols feitos e gols recebidos será melhor classificado;
- O quarto critério é o número de gols marcados. Se dois times empatam em todos os critérios anteriores, então o time que marcou mais gols será melhor classificado;
- O quinto critério é o número de partidas jogadas. Se dois times empatam em todos os critérios anteriores, então o time que realizou menos jogos até o momento será melhor classificado;
- O último critério é o nome do time. Se dois times empatam em todos os critérios anteriores, então o time com nome de menor ordem lexicográfica estará melhor classificado.

## Entrada

A entrada será uma descrição completa de vários campeonatos. Cada campeonato é um caso de teste.

O primeiro valor na entrada será um inteiro N indicando o número de campeonatos.

Cada campeonato é uma descrição dos times e de todos os jogos realizados. A descrição do campeonato começa com uma linha em branco (que você deve ler e descartar com um comando input). Na linha seguinte aparecerá o nome do campeonato, que é uma string sem espaços que você pode ler com input.

Em seguida, aparecerá um inteiro T indicando o número de times (1 < T ≤ 30), seguido de T palavras com os nomes dos times. Os nomes dos times podem conter letras maiúsculas e minúsculas, números, hífen e o caracter barra-baixa (_).

Após o nome do último time, haverá um inteiro G indicando o número de jogos realizados até agora.

Os G jogos serão descritos da seguinte forma: o nome de um time, o separador :, o número de gols marcados por esse time, o separador #, o nome do segundo time, o separador : e o número de gols marcados pelo segundo time. Por exemplo, a descrição Bananeiras:3#Sao_Pedro:2 indica que a equipe Bananeiras venceu o time do São Pedro por 3 a 2. Todos os gols são números não negativos menores que 20. Você pode presumir que todos os nomes que aparecem nos jogos são times que foram apresentados anteriormente. Nenhum time irá jogar contra si mesmo.

## Saída

Para cada campeonato, imprima primeiramente o nome do campeonato em uma linha. As próximas T linhas devem descrever os T times do campeonato, ordenados de acordo com as regras apresentadas anteriormente.

Para cada time, imprima uma linha com o seguinte formato:

[a] - Nome_do_time: [b] pontos, [c] jogos ([d]-[e]-[f]), d.g. [g] ([h]-[i])

Substituindo:

    [a] pela posição do time no placar
    [b] pelo total de pontos que o time conseguiu
    [c] pelo número de jogos que o time jogou
    [d] pelo número de vitórias
    [e] pelo número de empates
    [f] pelo número de derrotas
    [g] pela diferença de gols (marcados - sofridos)
    [h] pelo número de gols marcados
    [i] pelo número de gols sofridos

Imprima uma linha em branco após cada campeonato.

## Caso de Teste 1

# Entrada

1
-

Desempate_por_nomes
6
Ultimo
Posicao6
posicao5
Posicao4
O_vice
Campeao
6
Ultimo:1#Posicao6:2
Ultimo:2#Posicao6:1
posicao5:2#Posicao4:1
posicao5:1#Posicao4:2
O_vice:1#Campeao:2
O_vice:2#Campeao:1

Saída 

Desempate_por_nomes
1 - Campeao: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)
2 - O_vice: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)
3 - Posicao4: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)
4 - posicao5: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)
5 - Posicao6: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)
6 - Ultimo: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)

Caso de Teste 2
Entrada 

2
-

World_Cup_1998_-_Group_A
4
Brazil
Norway
Morocco
Scotland
6
Brazil:2#Scotland:1
Norway:2#Morocco:2
Scotland:1#Norway:1
Brazil:3#Morocco:0
Morocco:3#Scotland:0
Brazil:1#Norway:2
-

Some_strange_tournament
5
Team_A
Team_B
Team_C
Team_D
Team_E
5
Team_A:1#Team_B:1
Team_A:2#Team_C:2
Team_A:0#Team_D:0
Team_E:2#Team_C:1
Team_E:1#Team_D:2

Saída 

World_Cup_1998_-_Group_A
1 - Brazil: 6 pontos, 3 jogos (2-0-1), d.g. 3 (6-3)
2 - Norway: 5 pontos, 3 jogos (1-2-0), d.g. 1 (5-4)
3 - Morocco: 4 pontos, 3 jogos (1-1-1), d.g. 0 (5-5)
4 - Scotland: 1 pontos, 3 jogos (0-1-2), d.g. -4 (2-6)

Some_strange_tournament
1 - Team_D: 4 pontos, 2 jogos (1-1-0), d.g. 1 (2-1)
2 - Team_E: 3 pontos, 2 jogos (1-0-1), d.g. 0 (3-3)
3 - Team_A: 3 pontos, 3 jogos (0-3-0), d.g. 0 (3-3)
4 - Team_B: 1 pontos, 1 jogos (0-1-0), d.g. 0 (1-1)
5 - Team_C: 1 pontos, 2 jogos (0-1-1), d.g. -1 (3-4)

Caso de Teste 3

    Entrada 

    2
    -
    Torneio-dos-Programadores
    3
    Dijkstra
    Wirth
    Knuth
    4
    Dijkstra:1#Wirth:0
    Wirth:1#Knuth:1
    Dijkstra:2#Knuth:3
    Wirth:1#Dijkstra:0
    -
    Brasileirinho
    8
    Flamingo
    Sao_Pedro
    Bombeiros
    Aloha
    Coqueiros
    Pecadores
    Pedro_Cabral
    DTB
    12
    Flamingo:5#Sao_Pedro:0
    Bombeiros:3#Aloha:0
    Coqueiros:2#Pecadores:1
    Pedro_Cabral:1#DTB:1
    Flamingo:2#Coqueiros:1
    Sao_Pedro:3#Aloha:0
    Bombeiros:0#Pedro_Cabral:2
    DTB:1#Pecadores:2
    Coqueiros:3#Aloha:1
    Pecadores:3#DTB:0
    Pedro_Cabral:0#Flamingo:2
    Bombeiros:1#Sao_Pedro:2

    Saída 

    Torneio-dos-Programadores
    1 - Knuth: 4 pontos, 2 jogos (1-1-0), d.g. 1 (4-3)
    2 - Wirth: 4 pontos, 3 jogos (1-1-1), d.g. 0 (2-2)
    3 - Dijkstra: 3 pontos, 3 jogos (1-0-2), d.g. -1 (3-4)

    Brasileirinho
    1 - Flamingo: 9 pontos, 3 jogos (3-0-0), d.g. 8 (9-1)
    2 - Pecadores: 6 pontos, 3 jogos (2-0-1), d.g. 3 (6-3)
    3 - Coqueiros: 6 pontos, 3 jogos (2-0-1), d.g. 2 (6-4)
    4 - Sao_Pedro: 6 pontos, 3 jogos (2-0-1), d.g. -1 (5-6)
    5 - Pedro_Cabral: 4 pontos, 3 jogos (1-1-1), d.g. 0 (3-3)
    6 - Bombeiros: 3 pontos, 3 jogos (1-0-2), d.g. 0 (4-4)
    7 - DTB: 1 pontos, 3 jogos (0-1-2), d.g. -4 (2-6)
    8 - Aloha: 0 pontos, 3 jogos (0-0-3), d.g. -8 (1-9)
