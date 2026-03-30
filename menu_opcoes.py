
# 7. Desenvolva um programa que exiba na tela um menu de opções:

#    1 - Opção 1
#    2 - Opção 2
#    3 - Opção 3
#    4 - Sair
#    Digite uma opção: 
# Se o usuário digitar 1, exibir na tela: 'Você selecionou a opção 1'
# Se o usuário digitar 2, exibir na tela: 'Você selecionou a opção 2'
# Se o usuário digitar 3, exibir na tela: 'Você selecionou a opção 3'
# Se o usuário digitar 4, exibir na tela: 'Você selecionou sair'
# Se o usuário digitar uma opção diferente das apresentadas no menu, exibir 'Opção inválida!!!'
# Exibir no final do processamento 'Fim do programa!'

# menu de opções - imprimir para infomar o usuário
print("Menu de opções!")
# opção em número inteiro - int de 1-4 e input para inserir a opção desejada
opcao = int(input("Digite a opção desejada: "))
# estrutura condicionais if e elif para cada opção inserida
if opcao == 1:
    selecionada = "Você selecionou a Opção 1"
elif opcao == 2:
    selecionada = "Você selecionou a opção 2"
elif opcao == 3:
    selecionada = "Você selecionou a opção 3"
elif opcao == 4:
    selecionada = "Você selecionou sair"
#então - caso o usuário digitar a opção que não está disponível - variável = opção inválida
else:
    selecionada = "Opção inválida"
# print - mostrar qual opção foi selecionada
print(f"Menu de opções,{selecionada}")
#print - encerramento do programa - "Fim do programa"
print("Fim do programa")
