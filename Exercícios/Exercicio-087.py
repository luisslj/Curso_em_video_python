'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: '''
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

'''from random import randint
lista = []
matriz = []
for i in range(0,3):
    lista.append(int(randint(0,10)))
    lista.append(int(randint(0,10)))
    lista.append(int(randint(0,10)))
    matriz.append(lista[:])
    lista.clear()
for i in matriz:
    print(f'[ {i[0]} ][ {i[1]} ][ {i[2]} ]')
for i in lista:
    soma = sum(lista)
print(soma)
numeros = [10, 20, 30, 40]
total = sum(numeros)
print(total)  # Saída: 100'''

matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz1[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz1[l][c]:^5}]',end='')
        if matriz1[l][c] % 2 == 0:
            spar +=matriz1[l][c]
    print() 
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol +=matriz1[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz1[1][c]
    elif matriz1[1][c] > mai:
        mai = matriz1[1][c]    
print(f'o  maior da segunda linha é {mai}')





