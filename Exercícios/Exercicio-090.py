'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''


boletim = {}
boletim['nome'] = str(input('Nome do aluno: '))
boletim['media'] = float(input('Qual e a sua media: '))
if boletim['media']>= 7:
    boletim['situação'] = 'Aprovado'
elif 5 <= boletim['media'] < 7:
    boletim['situação'] = 'Recuperação'     
else:
    boletim['Situação'] = 'Reprovado'
print('-='*30)        
for i,v in boletim.items():
    print(f'{i} = {v}')
print('-='*30)    
print(boletim)
