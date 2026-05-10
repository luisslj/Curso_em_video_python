#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(num, t = 10):
    por = (num / 100) * t
    resultado = num + por
    return resultado

def diminuir(num, t = 10):
    por = (num /100) * t
    resultado = num - por
    return resultado

def metade(num):
    resultado = num / 2 
    return resultado

def dobro(num):
    resultado = num * 2
    return resultado

import moeda

num = float(input('Digite um numero:'))

print(f'O aumento de {num} e {moeda.aumentar(num)}.')
print(f'O diminutivo de {num} e {moeda.diminuir(num,15)}.')
print(f'O dobro de {num} e {moeda.dobro(num)}.')
print(f'A metade de {num} e {moeda.metade(num)}.')