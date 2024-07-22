data_completa = input("Digite a data (DD/MM/AAAA): ")

meses = {
        "01": "Janeiro", 
         "02": "Fevereiro", 
         "03": "Março", 
         "04": "Abril", 
         "05": "Maio",
         "06": "Junho",
         "07": "Julho",
         "08": "Agosto",
         "09": "Setembro",
         "10": "Outubro",
         "11": "Novembro",
         "12": "Dezembro"
         }

separadas = data_completa.split("/")

dia = separadas[0]
mes = separadas[1]
ano = separadas[2]

for i in separadas:
    print(i)


if mes in meses:
    nome_mes = meses[mes]
    print(f"Dia {dia} de {nome_mes} de {ano}")
else:
    print("Tem não")
