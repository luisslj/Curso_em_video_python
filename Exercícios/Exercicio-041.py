'''A confederação nacional de natação precisa de um programa
que leia o ano de nacimento de um atleta e mostre sua 
categoria, de acordo com a idade'''
# Até 9 anos:MIRIM
# Até 14 anos:INFANTIL
# Até 19 anos:JUNIOR
# Até 20 anos:SÊNIOR
# Acima:MASTER

ano = int(input('Digite o ano de nacimento! '))

idade = 2025 - ano

if idade <= 9:
    print(f'Você tem {idade} anos sua categoria é MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos sua categoria é INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos sua categoria é JUNIOR!')
elif idade <= 20:
    print(f'Você tem {idade} anos sua categoria é SÊNIOR!')
else:
    print(f'Vecê tem {idade} anos sua categoria é MASTER!')           