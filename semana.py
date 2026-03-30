# 4. Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'
# Qualquer outro numero exibir: 'Opção inválida!'
# variável semana - int para número inteiro e input para o usuário inserir o número que será validdo para a semana
semana = int(input("Digite um número de 1-7: "))
# condições para cada dia da semana associado com o número
if semana == 1:
    print("Domingo")
elif semana == 2:
    print("Segunda")
elif semana == 3:
    print("Terça")
elif semana == 4:
    print("Quarta")
elif semana == 5:
    print("Quinta")
elif semana == 6:
    print("Sexta")
elif semana == 7:
    print("Sábado")
# então - se o usuário digitar o valor inadequado,print - mostre: Opção inválida!
else:
    print("Opção inválida!")