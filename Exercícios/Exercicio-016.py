'''Crie um programa que leia um número real
qualquer pelo teclado e mostre na tela a sua parte inteira'''
#Exemplo digite o número:6.127
#O número 6.127 tem a parte interia 6.

from math import floor,trunc

num =float(input('Digite um valor '))

print(f'O número {num} tem a sua parte interia {trunc(num)}')

num1 = float(input('Digite um número '))

print(f'O número {num1} sua porção inteira e {int(num1)}')
