'''Faça um programa que leia o comprimento de um cateto
oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre 
o comprimento da hipotenusa'''

from math import hypot

co = float(input('Digite o cateto oposto!'))
aj =float(input('Digite o cateto adjacente!'))

h = hypot(co,aj)

print(f'A hipotenusa dos catetos e igual {h:.2f}')