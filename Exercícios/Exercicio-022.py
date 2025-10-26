'''Criar um programa que leia o nome
completo de uma pessoa e mostre:'''
# O nome com todas as letras maiúsculas
# O nome com todas Minúsculas.
# Quantas letras tem todo nome (sem considerar espaços).
# Quantas letras tem o primeiro nome

nome = ('Luis Souza Jacinto').strip()#str(input('Digite o nome completo! '))
print('Analisando seu nome...')
print(f'Nome com letras maiúsculas {nome.upper()}')
print(f'Nome com letras minúsculas {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')}')
print(f'Seu primeiro nome tem {nome.find(' ')}')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
