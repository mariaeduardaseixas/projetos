# 2. Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3
# residencia_normal.py
# input para inserir e float número decimal - o usuário vai inserir o valor dejedao
consumo = float(input(" Digite o consumo de água da residência normal em m³: "))
# linha 10 para mostrar o valor que foi digitado anteriormente
print(f"O consumo de água da residência normal é {consumo}")
# estruturas condicionais para cada caso usando o if,elif e else
if consumo <= 10:
    valor = 22.38
elif consumo <= 20:
    valor = consumo * 3.50
elif consumo <= 50:
    valor = consumo * 8.75
elif consumo > 50:
    valor = consumo * 9.64
else:
    valor = consumo * 22.38
#mostre o valor total com duas casas decimais.
print(f"O valor total é R$ = {valor:.2f}")