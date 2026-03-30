# 10 - Desenvolva um programa que pergunte em que turno você estuda. 
# Peça para digitar: M-Matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# Obs.: Somente letras maiúsculas para M, V ou N.

# Não esquecer que texto é entre aspas e definir cada letra
turno = input("Digite em turno você estuda M para Matutino,V para Vestino e N para Noturno: ")
M = "Matutino"
V = "Vespertino"
N = "Noturno"
if turno == "M":
    mensagem = "Bom dia!"
elif turno == "V":
    mensagem = "Boa Tarde!"
elif turno == "N":
    mensagem = "Boa Noite!"
#imprimir mensagem
print(f"Seja bem-vindo e {mensagem}")
