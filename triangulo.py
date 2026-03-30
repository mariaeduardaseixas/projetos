# 6. Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

# número de cada lado do triângulo

lado1 = float(input("Digite o 1 lado do triângulo: "))
lado2 = float(input("Digite o 2 lado do triângulo: "))
lado3 = float(input(" Digite o 3 lado do triângo: "))

# lados iguais - operadores relacionais == para o triângulo eqilátero que possui todos os lados iguais e criação da variável triângulo para todos os casos
if lado1 == lado2 == lado3:
    triangulo = "Triângulo Equilátero"
# else + if para se caso forem apenas dois lados iguais,resultando no triângulo isóceles
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    triangulo = "Triângulo Isóceles"
# elif para todos os lados diferentes != resultando em triêngulo escaleno
elif lado1 != lado2 != lado3:
    triangulo = "Triângulo Escaleno"
#print para imprimir mensagem | f - para formatar /inserir a variável triângulo na mensagem
print(f"De acordo com os números inseridos a forma geométrica é {triangulo}")


#Resposta em sua forma mais simples
print(f"O triângulo é {triangulo}")

