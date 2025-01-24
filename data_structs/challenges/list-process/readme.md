Lista de Processos

Qualquer processador, seja de um desktop, laptop ou smartphone, é capaz de executar vários programas ao mesmo tempo. Mesmo que o número de programas em execução seja maior que o número de processadores! Isso é possível pela técnica de "tempo compartilhado". Se existem vários programas em execução e um só processador, então o sistema permite a um programa qualquer fazer uso desse processador por alguns micro ou nanossegundos (um microssegundo equivale a 10-6 ou 0,000001 segundos). Após esse pequeno intervalo, outro programa é executado, depois outro e assim por diante. Isso dá ao usuário a impressão de que todos os programas estão executando ao mesmo tempo.

Uma forma de controlar quais programas fazem uso da CPU é criar uma lista circular encadeada, na qual cada nó representa um programa diferente. A lista é percorrida ininterruptamente. O "nó da vez" recebe permissão para fazer uso da CPU por algum tempo. Quando esse tempo termina, o sistema passa para o nó seguinte. Quando o sistema chega ao fim da lista, o primeiro programa volta a fazer uso da CPU. Daí a necessidade de uma lista circular.

Neste exercício, você simulará a execução de um conjunto de programas que compartilham um único processador. Para simplificar, suponha as seguintes restrições:

    A lista de programas é definida uma única vez e cada programa é identificado por um nome;
    Existe um parâmetro do sistema, chamado Q, que define a cota que cada programa tem para fazer uso da CPU quando chega sua vez. Quando um programa entra em execução, ele pode executar por Q microssegundos. Após esse tempo, é a vez do próximo programa da lista usar a CPU;
    Cada programa possui um tempo total que leverá para realizar suas tarefas. Quando o programa fizer uso suficiente da CPU, sua execução termina e ele sai da lista, mesmo que não tenha terminado de usar sua cota;
    Quando não houver mais programas para executar, o sistema desliga automaticamente.

Faça um programa principal que lê uma lista de programas e simula a execução de todos eles. Indique o instante em que cada programa finaliza e quando o sistema desliga.


Entrada

A entrada começa com dois inteiros, Q e N, indicando a cota do tempo compartilhado e o número de programas que serão simulados. Ambos são inteiros estritamente positivos.

Em seguida, haverá uma lista de programas. Cada programa possui um nome e um tempo total de execução. O nome será uma cadeia de até 80 caracteres que pode conter apenas letras minúsculas e hifens. O tempo total será um inteiro estritamente positivo.


Saída

Realize a simulação, executando cada programa por até Q microssegundos e verificando quando eles terminam. Durante a simulação, imprima os instantes, em microssegundos, nos quais cada programa finalizou e quando o sistema foi desligado. Use os seguintes padrões:

    %d us: %s finalizou; ou
    %d us: shutdown.

Note que o símbolo us representa o símbolo µs, a unidade de um microssegundo.


Exemplo comentado

Entrada:

30 2
hello-world 35
calc-fibonacci 100

Saída:

65 us: hello-world finalizou
135 us: calc-fibonacci finalizou
135 us: shutdown

Explicação:

A entrada começa com Q=30 e N=2, indicando que a cota de tempo compartilhado é 30µs e serão simulados 2 programas. Em seguida são descritos os dois programas, com seus nomes e tempos totais de execução.

Durante a simulação, os seguintes eventos ocorrem nos seguintes instantes:

Instante
	

Evento

0
	

O programa hello-world (H, para encurtar) é posto em execução.

30
	

Após executar por Q=30 microssegundos, o programa H esgota sua cota. O tempo remanescente de H agora é 5.

30
	

O programa calc-fibonacci (F, daqui pra frente) é posto em execução.

60
	

O programa F executa por Q=30 microsegundos e esgota sua cota. Seu tempo remanescente é 70.

60
	

O programa H é posto em execução.

65
	

Após rodar por mais 5 microssegundos, o programa H termina toda a sua execução. A mensagem 65 us: hello-world finalizou é impressa.

65
	

O programa H é tirado da lista.

65
	

O programa F é posto em execução.

95
	

O programa F executa por Q=30 microssegundos. Seu tempo remanescente agora é 40

95
	

O programa F é posto em execução.

125
	

O programa F executa por mais Q=30 microssegundos. Seu tempo remanescente é 10

125
	

O programa F é posto em execução.

135
	

Após 10 microssegundos, o programa F termina toda a sua execução. A mensagem 135 us: calc-fibonacci finalizou é impressa.

135
	

O programa F é tirado da lista.

135
	

Como não há mais programas em execução, o próprio sistema finaliza. A mensagem 135 us: shutdown é impressa.

Elabore uma lista duplamente encadeada circular. O fato de ser duplamente encadeada simplificará a remoção dos nós da lista.

O código inicial contém algumas funçõies que trazem a definição de lista na qual cada nó é uma dicionário para os programas. Elabore uma função que ajusta os ponteiros para inserir esse nó no final da lista.

Somente remova um nó da lista quando o programa tiver finalizado sua execução.
Caso de Teste 1
Entrada	

10 4
recursivo 11
fatorial 10
codebench 20
say-hello 1

Saída	

20 us: fatorial finalizou
31 us: say-hello finalizou
32 us: recursivo finalizou
42 us: codebench finalizou
42 us: shutdown

Caso de Teste 2
Entrada	

50 3
hello-world 17
fibonacci 235
numeros-primos 88

Saída	

17 us: hello-world finalizou
205 us: numeros-primos finalizou
340 us: fibonacci finalizou
340 us: shutdown

Caso de Teste 3
Entrada	

30 2
hello-world 35
calc-fibonacci 100

Saída	

65 us: hello-world finalizou
135 us: calc-fibonacci finalizou
135 us: shutdown