'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

from random import randint



list = []
list_par = []
list_ip = []
list.append (int(input('Digite um número: ')))
cont = ''
while True:
    cont = str(input('Quer continuar [S/N]: '))
    if cont in 'Ss':
        list.append  (int(input('Digite um número: ')))
    if cont in 'Nn':
        break    

for i in (list):
    if i % 2 == 0:
        list_par.append(i)
    if i % 2 > 0:
        list_ip.append(i)

print(f'Os itens da lista são {list}')
print(f'OS itens da lista par são {list_par}')
print(f'Os itens da lista inpar são {list_ip}')
