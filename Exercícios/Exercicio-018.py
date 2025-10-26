'''Faça um programa que leia um ângulo qualquer e 
mostre na tela o valor do seno, cosseno e tangente
desse angulo'''

import math

print('-'*40)
angulo = float (input('Digite o angulo ! '))

cose = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tanj = math.tan(math.radians(angulo))

print('-'*40)
print(f'O cosseno do ângulo {int(angulo)}° e {cose:.2f}')
print('-'*40)
print(f'O seno do ângulo {int(angulo)}° e {sen:.2f}')
print('-'*40)
print(f'A tangencia do ângulo {int(angulo)}° e {tanj:.2f}')
print('-'*40)
