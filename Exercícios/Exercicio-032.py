'''Faça um programa que leia um ano qualquer e mostre
se ele e um ano BISSEXTO.'''

from datetime import date #para saber o ano da maquna
ano = int(input('Digite um ano para saber se e BISSEXTO! '))

bis = ano % 400 == 0
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #formula para saber se é BISSEXTO
    print(f'O ano {ano} e um ano BISSEXTO!')
else:
    print(f'O ano {ano} não e BISSEXTO ') 

    
       