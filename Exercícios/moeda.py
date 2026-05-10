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

'''teste = 100
print(dobro(teste))
print(aumentar(teste))
print(diminuir(teste, 20))
print(metade(teste))'''
