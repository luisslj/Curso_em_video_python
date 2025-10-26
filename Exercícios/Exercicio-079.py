'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores 
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, 
serão exibidos todos os valores únicos digitados, em ordem crescente.'''

list = []

list.append(int(input('Digite um núemro:')))
cont = ''
while True:
    cont = str(input('Quer continuar [S/N]: '))
    if cont in 'Ss':
        list.append(int(input('Digite um núemro:')))
    if cont in 'Nn':
        break


for i in (list):
    if i == i in list:
        list.pop(i)

list.sort

print(list)