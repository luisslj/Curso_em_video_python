'''Faça um programa que leia o ano de nacimento de um jovem e 
informe, de acordo com a sua idade:'''
'''-Se ele vai se alistar ao srviso militar'''
'''-Se é a hora de se alistar.'''
'''-Se já passou do tempo de alistamento.'''
'''Seu programa também devéra mostrar o tempo que falta ou 
utrapassou do prazo'''

ano = int(input('Digite o ano de nacimento: '))

idade = 2025 - ano

if idade < 18:
    tempo = 18 - idade
    print(f'Sua idade e {idade} anos')
    print(f'Você vai se alistar daqui a {tempo} anos:')
elif idade == 18:
    print(f'Chegou a hora de se alistar, você ja tem {idade} anos!')
elif idade > 18:
    tempo = idade -18
    print(f'Sua idade e {idade} anos')
    print(f'você passou do tempo de alistamento {tempo} anos!')      


