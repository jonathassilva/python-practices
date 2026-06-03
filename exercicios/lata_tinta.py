area = float(input("Digite a área a ser pintada em metros quadrados: "))

area_com_margem = area * 1.10

litros_necessarios = area_com_margem / 6

preco_galao = 80.00
capacidade_galao = 18.0
preco_lata = 25.00
capacidade_lata = 3.6

galoes_necessarios = int(litros_necessarios // capacidade_galao)
litros_restantes = litros_necessarios - (galoes_necessarios * capacidade_galao)

if litros_restantes > 0:
    latas_necessarias = int(litros_restantes // capacidade_lata)
    if litros_restantes % capacidade_lata != 0:
        latas_necessarias += 1
else:
    latas_necessarias = 0


if litros_necessarios <= capacidade_galao:
    galoes_necessarios = 1
    latas_necessarias = 0
elif litros_necessarios <= capacidade_lata:
    galoes_necessarios = 0
    latas_necessarias = 1
else:
    if litros_restantes > 0 and litros_restantes <= capacidade_lata:
        latas_necessarias = 1
    elif litros_restantes > capacidade_lata:
        latas_necessarias = (litros_restantes // capacidade_lata) + 1

custo_total = (galoes_necessarios * preco_galao) + (latas_necessarias * preco_lata)

print(f"Área a ser pintada: {area} metros quadrados")
print(f"Litros necessários com margem: {litros_necessarios:.2f} litros")
print(f"Quantidade de galões: {galoes_necessarios}")
print(f"Quantidade de latas: {latas_necessarias}")
print(f"Custo total: R${custo_total:.2f}")
