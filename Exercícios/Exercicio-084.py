'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:'''
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


'''pessoa = []
dado = []
cadastro = 0
pessoa70 = []
pessoa100 = []
r = ''
print('-='*30)
print('FICHA DE CADASTRO')
print('-='*30)
while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Dogite seu peso: ')))
    r = str(input('Quer continuar [S/N]: '))
    pessoa.append(dado[:])
    dado.clear()
    cadastro += 1
    if r in 'Nn':
        break
print('-='*30)    

pessoa.sort()
print(f'Forão cadastradas {cadastro}.')
for i in pessoa:
    if i[1] >= 100:
        pessoa100.append(i)
        print(f'{i[0]} tem {i[1]} e está acima do peso.')
    if i[1] <= 70:
        pessoa70.append(i)
        print(f'{i[0]} tem {i[1]} e está abaixo do peso.')   
print('-='*30)
'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = temp = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1]< men:
            men = temp[1]
    princ.appemd(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break             
print('-='*30)
print(f'ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        princ(f'[{p[0]}]', end='')
print()               