import datetime
import calendar

def formatar_data(data):
    try:
        data_obj = datetime.datetime.strptime(data, "%d/%m/%Y")
        
        dia = data_obj.day
        mes = data_obj.month
        ano = data_obj.year

        mes_por_extenso = calendar.month_name[mes]

        return f"{dia} of {mes_por_extenso} of {ano}"
    except ValueError:
        return None

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
data_formatada = formatar_data(f"{dia}/{mes}/{ano}")
if data_formatada:
    print(data_formatada)
else:
    print("Data inválida")
