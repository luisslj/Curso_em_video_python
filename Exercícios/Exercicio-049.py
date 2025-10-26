'''Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Digite um número para taboada: '))

for i in range(1, 11):
     print(f'{i} X {num} = {num * i}')
