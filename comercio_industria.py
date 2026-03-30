# 3. Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3
# comercio_industria.py
# o usuário irá inserir o valor de consumo da água para prédios comerciais e industriais - input e poderá ser números quebrados - float | variável - consumo
consumo = float(input(" Digite o consumo de água para prédios comerciais e industriais em m³: "))
# mostra as informações que foram inseridas através do print e formato
print(f"O consumo é {consumo}")
# criação de cada condição,utilizando if - se | elif else + if|else - então 
# se consumo é igual/menor/maior que um número,mostre o determinado valor(variável)
if consumo <= 10:
    valor = 44.95
elif consumo <= 20:
    valor = consumo * 8.75
elif consumo <= 50:
    valor = consumo * 16.76
elif consumo > 50:
    valor = consumo * 17.46

# saída - print - mostrar o valor total 
print(f"O valor total é R$ = {valor:.2f}")