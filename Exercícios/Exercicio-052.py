'''Faça um programa que leia um número interio e diga 
se ele e ou não um número primo'''

n = int(input('Digite um número qualquer: '))
total = 0

for c in range(1, n +1):
    if n % c == 0:
        print('-', end=' ')
        total += 1 
    else:
        print('*', end=' ')    
    print(f'{c}', end=' ')   

print(f'O número {n} foi divisível {total} vezes')
if total == 2:
    print(f'O número {n} e um número primo')
else:
    print(f'O número {n} não e um número primo')    