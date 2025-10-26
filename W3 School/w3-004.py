'teste de senha'


import random

import time

inicio = time.time()

computador = random.randint(1000,9999)
palpite = 0 #int(input('Digite um número qualque: '))


print(computador)

c = 0

while computador != palpite:
   # palpite = int(input('Digite um número qualque: '))
     palpite = random.randint(1000,9999)
     print(palpite)
     c = c + 1

fim = time.time()

print(f'tempo que o programa demorou {fim - inicio:.2f} segundos')
print(f'Número de tentativas {c}')
print(f'A senha e {computador}')     


