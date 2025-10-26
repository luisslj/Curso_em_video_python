'''Faça um programa que leia o nome completo de uma pessoa ,
mostrando em seguida o primeiro e o ultimo nome separadamente.'''
#Ex:Ana Maria de Souza
#Primeiro nome:Ana
#Ultimo nome: Souza

nome = str(input('Digite seu nome completo! '))

nome = nome.split()
print('Muito prazer em te conhecer!')
print(f'O seu primeiro nome e {nome[0]}: ')
print(f'O seu último nome e {nome[-1]}:')
print(nome[len(nome)-1])
