'''Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. O programa vai perguntar o valor 
da casa, o salário do comprador e em quantos anos ele vai pagar.'''
'''Calcule o valor da prestação mensal sabendo que ela não 
pode exceder 30% do salário ou então o empréstimo será negado.'''

import math
#porcentagem (valor*15/100)
print('Analise de credito...')
print('-='*30)
casa = float(input('Digite o valor da casa! R$ '))
salario = float(input('Digite o seu salário! R$ '))
ano = int(input('Digite em quantos anos! R$ '))
print('-='*30)

meses = ano * 12
parcela = casa / meses
salario30 = salario * 30 / 100

if parcela <= salario30:
    print('esta aprovado')
    print(f'para pagar uma casa de R${casa} em {ano} será de meses R${parcela:.2f}')
else:
    print('O valor da parcela passa de 30% do seu salario')
    print(f'para pagar uma casa de R${casa} em {ano} será por mês R${parcela:.2f}')
    print('Empréstimo NEGADO!')
print('-='*30)    
