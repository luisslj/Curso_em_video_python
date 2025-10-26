'''Crie um programa que leia o ano de nacimento de sete pessoas.
no final mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores '''
from datetime import date
ano = int(input('Digite o ano que naceu: '))
atual = date.today().year
idade = atual - ano

menor = 0
maior = 0
i = 0

for i in range(1,3):
    ano = int(input('Digite o ano que naceu: '))
    if idade >= 21:
        maior += 1
    else: 
        menor += 1

print(maior)    