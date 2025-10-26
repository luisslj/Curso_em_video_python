'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {}

jogo['Jogador1'] = randint(1,6)
jogo['Jogador2'] = randint(1,6)
jogo['Jogador3'] = randint(1,6)
jogo['Jogador4'] = randint(1,6)
print('-='*30)
for i,v in jogo.items():
    print(f'{i} = {v}')
print('-='*30)

ordedado = dict(sorted(jogo.items(), key = lambda item: item[1],reverse= True)) # comando para ordenar lista
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)# comando para ordenar lista 

for i,v in ordedado.items():
    print(f'{i} = {v}')
print('-='*30)    
