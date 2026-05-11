#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31m ERRO: Por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n    

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31m ERRO: Por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n    





num = LeiaInt('Digite um número: ')
num1 = LeiaFloat('Digite um número: ')
print(f'O valor digitado foi {num}')