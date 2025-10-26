'''Melhore o jogo do Desafio 028 onde o computadorvai Pensar em 
um número entre 0 e 10.Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import choice,randint

'''computador = randint(0,10)
print('-='*25)
print('Jogo da Adivinhação')
print('-='*25)
palpite = int(input('Digite um número qualque: '))

print(computador)

while computador != palpite:
     print('-='*25)
     palpite = int(input('Digite um número qualque: '))
     if palpite == computador:
      print('-='*25)
      print('Parabens você acertou!!!')
      print('-='*25)
     else:
      print('-='*25)
      print('Você Errou tente novamente!!!') '''

computador = randint(0,10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpeite: '))
    palpites += 1
    if jogador == computador:
        acertou= True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menor... Tente mais uma vez: ')
print(f'Acertou com {palpites} tentativas Parabéns!')            
          


