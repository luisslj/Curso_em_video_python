#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto():
    ano = int(input('Digite o ano de nacimento: '))
    idade = 2026 - ano
    if 16 > idade:
        print("O voto esta negado")
        print(idade)
    elif 18 <= idade < 65:
        print('O voto e obrigatorio')
        print(idade)
    else:
        print('O voto e Opcinal')
        print(idade)


voto()