'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''

def Area(a,b):
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    t = a * b
    print(f'A área de um terreno {a}x{b} é de {t}m²')

Area(0,0)

