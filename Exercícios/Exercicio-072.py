'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente 
preenchida com uma contagem por extenso, de zero até vinte. Seu programa 
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''


numeros = ('Zero', 'um', 'Dois', 'Treis', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'dez', 'Onze', 'Doze')
cont = ''
while True:
    num = int(input('Digite um número de 0 a 20: '))
    while num < 0 or num > 20:
        num = int(input('número invalido. Digite novamente outro número: '))
    #print(numeros.index(0))
    if num >= 0 or num <= 20:
        print(numeros[num])
        cont = str(input('Quer continuar o programa [S/N]: '))
    if cont == 'N':
        break

'''#Exercício 072 - Número por Extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[num]}.')'''