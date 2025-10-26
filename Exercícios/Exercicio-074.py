'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
 e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também 
indique o menor e o maior valor que estão na tupla.'''

from random import choices,randint

num1 = randint(1,10)
num2 = randint(1,10)
num3 = randint(1,10)
num4 = randint(1,10)
num5 = randint(1,10)

numero = (num1, num2, num3, num4, num5)

print(numero)

print(max(numero))
print(min(numero))   

numeros = ((randint(1,10)),  (randint(1,10)),  (randint(1,10)) ,(randint(1,10)))
print('Os valores sorteados foram ' , end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')    