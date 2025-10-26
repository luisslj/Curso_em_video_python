'''Crie um programa que faça o computador 
jogar Jokenpô com você.'''

from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int (input('Qual é a sua jogada? '))
print('-='*11)
print(f'computador jogou {(itens[computador])}')
print(f'Jogador jogou {(itens[jogador])}')
print('-='*11)

if computador == 0:
    if jogador ==0:
