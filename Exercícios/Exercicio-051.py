'''Desenvolva um programa que leia o primeiro termo e a razão
de um PAprogreção aritimetica.No final, mostre os 10 primeiros 
termos dessa progreção. '''

print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

pt = int(input('Digite o primeiro termo: '))#primeiro termo
r = int(input('Digite a razão: '))#razão
t = pt + ((10-1) * r)#termo
c = 0

for i in range(pt, t+1, r):
    print(i,end='-')
    c += 1

print(f'{c}° termo')    