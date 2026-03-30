# 9 - Desenvolva um programa que leia o valor (R$) de um salário qualquer e calcule e exiba o desconto com IRRF e INSS;
# fonte: https://impostoderenda2023.com.br/tabela-do-imposto-de-renda-2023/

# INSS (progressivo)
# Até 1.302,00 → 7,5%
# 1.302,01 até 2.571,29 → 9%
# 2.571,30 até 3.856,94 → 12%
# 3.856,95 até 7.507,49 → 14%
# IRRF
# Até 1.903,98 → isento
# 1.903,99 até 2.826,65 → 7,5% (–142,80)
# 2.826,66 até 3.751,05 → 15% (–354,80)
# 3.751,06 até 4.664,68 → 22,5% (–636,13)
# Acima de 4.664,68 → 27,5% (–869,36)



salario = float(input("Digite o seu salário: "))

if salario <= 1320:
    inss = salario * 0.075
elif salario <= 2571.29:
    inss = salario * 0.09
elif salario <= 3856.94:
    inss = salario * 0.12
else:
    inss = salario * 0.14

# IRRF
base = salario - inss

if base <= 1903.98:
    irrf = 0
elif base <= 2826.65:
    irrf = base * 0.075
elif base <= 3751.05:
    irrf = base * 0.15
else:
    irrf = base * 0.225

# Salário líquido
liquido = salario - inss - irrf

print("Salário bruto:", salario)
print("INSS:", inss)
print("IRRF:", irrf)
print("Salário líquido:", liquido)