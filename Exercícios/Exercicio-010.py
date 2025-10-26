'''Crie um programa que leia quanto 
dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar
'''
# considrar US$ 1,00 = R$ 5,54

rs = float(input('Digite o quanro de dinheiro tem na carteira! '))

us = rs / 5.54

print(f'Com esse dinheiro e possivel comprar US$ {us:0.3} Dolares!')