# 5. Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: 
# imc = peso / altura ^ altura
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave'
# 16 a < 17	'Magreza moderada'
# 17 a < 18,5	'Magreza leve'
# 18,5 a < 25	'Saudável'
# 25 a < 30	'Sobrepeso'
# 30 a < 35	'Obesidade Grau I'
# 35 a < 40	'Obesidade Grau II (severa)'
# ≥ 40		'Obesidade Grau III (mórbida)'
# duas variáveis para indicar o valor da altura e o peso

import math

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
# processamento -imc - conta utilizada para saber o seu bem-estar através da altura e peso.
imc = peso / (pow(altura, 2))
print(imc)
#avaliação do imc
if imc <= 16:
    resultado = "Magreza grave"
elif imc <= 17:
    resultado = "Magreza moderada"
elif imc <= 18.5:
    resultado = "Magreza leve"
elif imc <= 25:
    resultado = "Saudável"
elif imc <= 30:
    resultado = "Sobrepeso"
elif imc <= 35:
    resultado = "Obesidade Grau I"
elif imc <= 40:
    resultado = "Obseidade Grau II (Severa)"
elif imc > 40:
    resultado = "Obesidade Grau III"
# indicação do sistema para outros casos
else:
    print("Tome cuidado com sua saúde")
# mostrar o resultado de saúde
print(f"O seu IMC é = {resultado:}")


