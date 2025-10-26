'''Crie um programa que leia o nome
de uma pessoa e diga se ela tem Silva no nome'''
nome1 = str(input('Qual e seu nome? '))
print(f'Seu nome tem Silva? {('silva' in nome1.lower())}')

print('-'*40)
nome = str (input('Digite um nome qualquer! '))

if 'silva' not in nome.lower():
    print('Não tem Silva no nome')
else:
    print('Você tem o nome Silva!')    