'''Crie um programa que leia um número inteiro
e mostra na tela se ele é PAR ou IMPAR.'''

# Solicita que o usuário digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar usando o operador de módulo (%)
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")