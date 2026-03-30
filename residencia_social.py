# Exercícios Estruturas de Decisão I
# ********** ********** ** *******
# Obs.: m3 = metro(s) cúbico(s)

# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3
# residencia_social.py
# primeiro declaramos uma variável chamada consumo para definir o consumo de água da residência social
consumo = float(input("Digite o consumo de água da residência social em m³: "))
# print foi utilizado para imprimir o valor do consumo
print(f"O consumo de água é {consumo}") 
# if = se,se o consumo depois operadoradores relacionais,por último o valor desejado com :
#variável valor para determinar | elif múltiplas opções | else: então para finalizar com outra opção

if consumo <= 10:
    valor = 7.59
elif consumo <= 20:
    valor = consumo * 1.31
elif consumo <= 30:
    valor = consumo * 4.64
elif consumo <= 50:
    valor = consumo * 6.62
elif consumo > 50:
    valor = consumo * 7.31
else:
    valor = consumo * 7.59
# f formatar a variável valor :.2f 2 casas decimais
print(f"O valor total será de R$ = {valor:.2f}")


