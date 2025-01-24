Ordenação de Pontos por Mesclagem

Crie uma classe representar um ponto que possa depois ser usada para ordenar uma lista de pontos no plano cartesiano. Além de criar o construtor, você deverá sobrecarregar o método __lt__ de modo que seja possível ordenar os pontos, usando necessariamente o algoritmo Merge Sort, de acordo com os seguintes critérios:

    O ponto mais próximo da origem deve aparecer primeiro. Por exemplo, (2, 2) está mais perto da origem do que (0, 3);
    Se dois pontos estiverem à mesma distância da origem, o ponto que estiver mais à esquerda vem primeiro. Exemplo: (0, 5) e (3, 4);
    Se os dois pontos estiverem à mesma distância da origem e possuírem o mesmo valor da coordenada x, então o ponto que estiver mais abaixo vem primeiro. Exemplo: (6, -8) e (6, 8).

O nome da sua classe deverá ser ponto e ela deverá conter os seguintes métodos:

    __init__(self, x, y): o construtor deverá receber as coordenadas do ponto e guardar os atributos self.x e self.y, além de calcular e armazenar a distância do ponto para a origem;
    __lt__(self, outro): este método sobrecarregará o operador < e será usado para fazer comparações entre pontos. Ele deverá receber como argumento um outro objeto da classe ponto e retornar True se e somente se o ponto representado por self deve aparecer antes do que o ponto representado por outro.

Em seguida, faça um programa principal que lê uma série de pontos e os guarda em uma lista para em seguida ordená-los. Você deve, necessariamente, utilizar o algoritmo de ordenação Merge Sort. O seu algoritmo de ordenação não deve fazer comparações de distâncias ou coordenadas. Em vez disso, o seu algoritmo deve apenas comparar dois pontos. O método __lt__, sobrecarregado, é quem verificará os critérios da ordenação.

A entrada será uma lista contendo N tuplas. Cada tupla representa as coordenadas de um ponto no plano cartesiano.

Imprima a coleção ordenada usando o formato ilustrado nos casos de exemplo.

    O seu algoritmo Merge Sort deve ser "agnóstico" ao tipo de dados que está ordenando. Isto é, ele deve apenas comparar dois elementos da lista, sem "saber" se eles são pontos, inteiros, strings ou outro tipo de dados.
    Reutilize a implementação do Merge Sort que você elaborou no exercício anterior!
    Dado um ponto p=(x,y), sua distância à origem é x2+y2

    ​.

Caso de Teste 1
Entrada	

[(0, 1), (3, 4), (-6, 8)]

Saída	

0 1
3 4
-6 8

Caso de Teste 2
Entrada	

[(-1, 0), (-1, 68), (0, 1), (15, -55), (15, 20)]

Saída	

-1 0
0 1
15 20
15 -55
-1 68

Caso de Teste 3
Entrada	

[(1,0), (4,0), (9,0), (0,-2), (0,-5), (0,-10), (1,1), (2,2), (-1,2), (-2,3), (-3,-3), (-3,-5)]

Saída	

1 0
1 1
0 -2
-1 2
2 2
-2 3
4 0
-3 -3
0 -5
-3 -5
9 0
0 -10