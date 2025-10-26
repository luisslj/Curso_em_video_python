'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores númericos 
e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

from random import randint
list = []

for i in range(0,5):
    list.append(randint(0,10))

print(list)


