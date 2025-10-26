'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

'''print('-='*30)
print('JOGADA NA MEGA SENA')
print('-='*30)
num = int(input('Quantos Jogos Você que jogar:'))
palpite = list()
lista = list()
print('-='*30)
for i in range(0,num):
    palpite.append(randint(0,60))
    palpite.append(randint(0,60))
    palpite.append(randint(0,60))
    palpite.append(randint(0,60))
    palpite.append(randint(0,60))
    palpite.append(randint(0,60))
    lista.append(palpite[:])
    palpite.clear()
computador = list()  
for i in range (0,6):
    computador.append(randint(0,60))    

for i in lista:
    print(i)
    if palpite in lista:
        lista.clear()
        print(i)
        print('Número repitido')
    if computador in lista:
        print('Parabéns Você e o vencedor')

print(f'Resultado {computador}')'''

lista = list()
jogos = list()
print('-' *30)
print('    JOGA NA MEGA SENA    ')
print('-' *30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3,f'SORTEANDO {quant} JOGOS', '-='*3)
for i,l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, 'BOA SORTE!', '-=' *5)
    