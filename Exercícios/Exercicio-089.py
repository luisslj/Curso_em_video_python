'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que
o usuário possa mostrar as notas de cada aluno individualmente.'''
'''print('-='*30)
print('Cadastro do boletim de notas')
print('-='*30)
boletim = []
dado = []
cont = ''

while True:
    dado.append(str(input('Digite o nome do aluno: ')))
    dado.append(float(input('Digite a primeira nota:')))
    dado.append(float(input('Digite a segunda nota: ')))
    cont= str(input('Quer cintinuar o cadastro [S/N]: '))
    boletim.append(dado[:])
    dado.clear()
    if cont in 'Nn':
        break


for i in boletim:
    print(f'o noe do aluno {boletim[i][0]} a media da sua nota e {media}')
    media = (boletim[i][1] + boletim[i][2]) / 2'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
    
print('-=' *30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...') 
        break
    if opc <= len(ficha) -1:
        print(f'Nota de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')               



