'''Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não formar um triangulo.'''
#r1
#r2
#r3
from time import sleep
print('-='*25)
print('Analisador de triângulos...')
print('-='*25)
r1 = float (input('Digite a reta 1! '))
r2 = float (input('Digite a reta 2! '))
r3 = float (input('Digite a reta 3! '))

print('Analisando...')
sleep(2)
if r1 < r2+r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os segumentos acima PODEM FORMAR triângulo')
else:
    print('OS seguimentos acima NÃO PODEM FORMAR')    

