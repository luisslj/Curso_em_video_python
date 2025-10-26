'''Escreva um programa que leia a velocidade de um 
carro'''
#Se ele utrapassar 80km/h,mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

vel = float(input('Digite a velocidade que passou! '))

lim = 80

valor = (vel - lim) * 7

if lim < vel:
    print('Você foi multado')
    print(f'valor da multa {valor}')
else:
    print('tenha um bom dia e dirija com segurança!')
