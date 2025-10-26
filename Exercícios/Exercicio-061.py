'''Refaça o desaafio 051, lendo o primeiro termo de uma razão
de uma PA, mostrando os 10 primeiro termos da progressão
usando a estrutura while.'''

print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Digite o primeiro termo: '))#primeiro termo
razao = int(input('Digite a razão: '))#razão
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}-',end='')
    termo += razao
    cont += 1
   

print('FIM') 