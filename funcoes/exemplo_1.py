def cabecalho(titulo, caracter = '-'):
    print(40 * caracter)
    print(titulo)
    print(40 * caracter)


cabecalho("Marketing")

palavra = "Financeiro"
simbolo = '$'
cabecalho(palavra, simbolo)

cabecalho('Logistica', caracter='*')
