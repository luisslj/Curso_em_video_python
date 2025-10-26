'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
'''print('-='*30)
print('FICHA DE CADASTRO')
print('-='*30)
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['ano'] = int(input('Ano de nacimento: '))
cadastro['idade'] = 2025 - cadastro['ano']
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] == 0:
    print('')
else:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário:R$ '))
    cadastro['Aposentadoria'] = ((35)-(2025-cadastro['contratação'])) + cadastro['idade']
print('-='*30)
print(cadastro)
print('-='*30)
print(f'Nome tem valor {cadastro["nome"]}')
print(f'Idade tem valor {cadastro["idade"]}')
if cadastro['ctps'] == 0:
    print('')
else:
    print(f'ctps te valor {cadastro["ctps"]}')
    print(f'Contratação tem o valor {cadastro["contratação"]}')
    print(f'Salário tem o valor {cadastro["salario"]}')
    print(f'Aposentadoria tem o valor {cadastro["Aposentadoria"]}')
print('-='*30)'''
from datetime import datetime
dados = dict()
dados ['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nacimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação']+35)- datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  -{k} tem valor {v}')
        