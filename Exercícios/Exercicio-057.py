'''Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valores "M" ou "F". caso esteja errado, peça a digitação
novamente até ter um valor correto.'''



'''s = ''

while s != 'F' and s != 'M':
      s = input('Digite F/M para o cadastro do seu sexo: ').strip().upper()[0]
      if s != 'F' and s != 'M':
         print('Sexo invalido digite novamente!')
      else:
        print('Cadastro, feito com sucesso!')   



print('Fim')'''

sexo = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} Registrado com sucesso')

