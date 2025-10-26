'''Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobror qual foi o número
escolhido pelo computador.'''
# Oprograma deverará escrever na tela se usuário venceu ou perdeu

from random import choice,randint
from time import sleep

print('-='*40)
print('Vou pensar rm um número entre 0 e 5. Tente adivinhar')
print('-='*40)
num = int(input('Em que número eu pensei! '))

#list = [0,1,2,3,4,5]
com = randint(0,5)
print('Processando')
sleep(3)
if com == num:
    print(f'Você acertou o número {com} parabêns!!!')
else:
    print(f'Você errou tente o número {com} novamente!!!')