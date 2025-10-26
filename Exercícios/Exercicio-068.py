'''Faça um programa que jogue par ou impar com o computador. O jogo só será 
interrompido quando o jogador PERDER, mstrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random

impar = 0
par = 0
computador = 0
valor = 0
jogador = 'l'
cont = 0

print('-='*30)
print('VAMOS JOGAR PAR OU IMPAR')

while True:
    valor = int (input('Diga um valor: '))
    jogador = str (input('Par ou Impar?[I/P] '))
    computador = random.randint(1, 10)
    resultado = computador + valor
    
    print('-'*30)
    if resultado % 2 == 0:
        total = 'PAR'
    if resultado % 2 != 0:
        total = 'IMPAR'    
    print(f'Você Jogou {valor} e o computador {computador}. total deu {total}')
    print('-'*30)
    if jogador == 'p':
        if resultado % 2 == 0:
            print('Você VENCEU !!!')
            print('Vamos jogar novamente...')
        elif resultado % 2 != 0:
            print('Você PERDEU !!!')
            break
    if jogador == 'i':
        if resultado % 2 != 0:
            print('Você VENCEU!!!')
            print('Vamos jogar novamente...')
        elif resultado % 2 != 0:
            print('Você PERDEU !!!')
            break   
    cont += 1       

print(f'GAME OVER! você venceu {cont} vezes.')


