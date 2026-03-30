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


# prferência de escolha - adicione com input
escolha = input("Digite o número da operação (1/2/3/4/5): ")
# in - subconjunto em python como listas,tuplas
if escolha in ('1', '2', '3', '4','5','6','7'):

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

        
    if escolha == '1':
            print(f"Resultado: {num1 + num2}")
        
    elif escolha == '2':
            print(f"Resultado: {num1 - num2}")
        
    elif escolha == '3':
            print(f"Resultado: {num1 * num2}")
    elif escolha == '4':
             num2 != 0:
                print(f"Resultado: {num1 / num2}")
    elif escolha == '5':
             print(f"resultado: {num1 ** num2}")
    elif escolha == '6';
        print(pow(num1, num2))
elif escolha == '7':
    num1 % 2:
    print("Par")
else: 
    print("Ímpar")
        
    else:
                print("Erro: Divisão por zero! número ímpar")
else:
        print("Opção inválida!")

# else - erro e opção inválida

