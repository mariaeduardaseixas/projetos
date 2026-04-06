# 8. Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:

#    1 - Adição
#    2 - Subtração
#    3 - Multiplicação
#    4 - Divisão
#    5 - Potência
#    6 - Raiz quadrada
#    7 - Número par
#    8 - Número ímpar

# num1 = float(input("Digite o primeiro número para realizar o calcúlo: "))
# num2 = float(input("Digite o segundo número para realizar o cálculo: "))

# operacao = input("Digite a operação desejada: ")
# adicao = 1
# subtracao = 2
# multiplicacao = 3
# potencia = 4
# raiz_quadrada = 5
# divisao = 6



# if operacao == 1:
#     resultado = num1 + num2
# tipo booleano
# valores possíveis true 1 ou false = 0
# break para execução do programa

# prferência de escolha - adicione com input
import math
print("CALCULADORA")
print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potência\n6 - Raiz qudrada\n7 - Número par\n8 - Número ímpar")

# prferência de escolha - adicione com input
import math
print("CALCULADORA")
print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potência\n6 - Raiz qudrada\n7 - Número par\n8 - Número ímpar")

escolha = input("Digite o número da operação (1-8): ")
# in - subconjunto em python como listas,tuplas
if escolha in ('1', '2', '3', '4','5'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
elif escolha in ['6','7','8']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = None

match escolha:
    case '1':
        print(f"num1 + num2 = : {num1 + num2}")
    case '2':
        print(f"num1 - num2 = : {num1 - num2}")
    case '3':
        print(f"num1 * num2 = : {num1 * num2}")
    case '4':
        if num2 != 0:
            print(f"num1 / num2 = : {num1 / num2}")
        else:
            print(f"Erro: Não é opssível dividir por zero")
    case '5':
        print(f"num1 ^ num2 = : {pow(num1, num2)}")
    case '6':
        if num1 >= 0:
            print(f"Raiz quadrada = {math.sqrt(num1)}")
        else: 
            print("Erro: raiz quadrada de número negativo: ")
    case '7':
        if num1 % 2 == 0:
            print(f"O número {num1} é par!")
        else: 
            print(f"O número {num1} não é par ")
    case '8':
        if num1 % 2 == 1:
           print(f"O número {num1} é ímpar!") 
        else:
            print(f"O número {num1} não é ímpar")
    case '9':
        print("Opção inválida")

# else - erro e opção inválida

