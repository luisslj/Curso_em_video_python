'''Faça um programa que mostre na tela um contagem de fogos de 
artificio. indo de 10 até 0, com uma pausa de 1 segundo entres ela''' 

import time
from time import sleep

for i in range(10, -1, -1):
    sleep(1)
    print(i)
print('Feliz ano novo!!!')