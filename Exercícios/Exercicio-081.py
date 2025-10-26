'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:'''
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


list = []

list.append(int(input('Digite um número: ')))
cont = 0

while True:
    cont = str(input('Quer continuar [S/N]: '))
    if cont in 'Ss':
        list.append(int(input('Digite outro número: ')))
    if cont in 'Nn':
        break

print(f'O número de itens na lista e de {len(list)}')# contar quantos itens tem na lista 
list.sort(reverse =True)# deixar a lista em ordem decresente 
print(f'A lista Decresente {list}')


if 5 in list:
    print('tem o número 5')
else:
    print('não tem o número 5')    