'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

'''num = list()
inpar = list()
par = list()

for i in range(0,7):
    num.append(int(input('Digite um número: ')))
    if i % 2 == 0:
        par.append(i)
    if i % 2 == 1:
        inpar.append(i)    

print('-='*30)
num.sort()
print(f'A lista e {num}')
print(f'A lista de inpar e {inpar}')
print(f'A lista de par e {par}')
print('-='*30)'''

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()        
print('-='*30)
print(f'Todos os valores: {num}')  
print(f'{num[0]}')
print(f'{num[1]}')
