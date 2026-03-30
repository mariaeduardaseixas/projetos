# 12. Desenvolva um programa que leia quatro notas bimestrais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média final. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 8.9         B
#   Entre 6.0 e 7.4         C
#   Entre 4.0 e 5.9         D
#   Entre zero e 3.9        E
# O programa deve exibir na tela:
#   1. As quatro notas bimestrais,
#   2. A média final,
#   3. O conceito correspondente e,
#   4. A mensagem "APROVADO" ou "Reprovado" de acordo com a regra a seguir:
#      4.1. Se o conceito       for A, B ou C    exibir "APROVADO"
#      4.2. Senão se o conceito for D ou E       exibir "REPROVADO"

# notas do bimestre do estudante
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
# cálculo de média
media = (n1 + n2 + n3 + n4) / 4
# demonstracão de notas
if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"
# Aprovado ou reprovado
if conceito == "A" or conceito == "B" or conceito == "C":
    print("APROVADO")
else:
    print("REPROVADO")

print("Média:", media)
print("Conceito:", conceito)