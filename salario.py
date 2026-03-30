#  Desenvolva um programa que recebe o salário de um funcionário e determine o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 1000,00 (incluindo)     : aumento de 20%
#   salários até R$ 1.700,00                : aumento de 15%
#   salários até R$ 2.300,00                : aumento de 10%
#   salários acima de R$ 2.300,00 em diante : aumento de 5%

# Após o processamento exibir na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

# Exemplo:
# Salário digitado: R$ 1.900,00
# Aumento         : 10%
# Valor do aumento: R$ 190,00
# Novo salário    : R$ 2.090,00






# salario - valor do salario

salario = float(input("Digite o salário: R$ "))

# condições
if salario <= 1000:
    percentual = 20
elif salario <= 1700:
    percentual = 15
elif salario <= 2300:
    percentual = 10
else:
    percentual = 5

# aumento do salário
aumento = salario * percentual / 100
novo_salario = salario + aumento


print(f"Salário: R$ {salario:.2f}")
print(f"Novo salário    : R$ {novo_salario:.2f}")