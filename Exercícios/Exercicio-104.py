#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')


def leiaint(num):
    num = str(input())
    if num.isnumeric():
        return print(num)
    else:
       return print('Erro não e um numero')

#Programa principal

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')