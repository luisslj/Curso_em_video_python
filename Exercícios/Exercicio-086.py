'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e 
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

from random import randint

lista = []
matriz = []

for i in range(0,3):
    lista.append(randint(0,10))
    lista.append(randint(0,10))
    lista.append(randint(0,10))
    matriz.append(lista[:])
    lista.clear()

for i in matriz:
    print(f'[ {i[0]} ][ {i[1]} ][ {i[2]} ]')

matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):
        matriz1[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz1[l][c]:^5}]',end='')
    print()            

