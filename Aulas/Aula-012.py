#Curso Python #012 - Condições Aninhadas

nome = str(input('Digite seu nome! '))

nome1 = 'Luis'


if nome == nome1:
    print('seu nome e lindo!')
elif nome == 'Pedro' or nome =='Lucas' or nome =='Juliano':
    print('seu nome e especial!')
elif nome == 'Maria' or nome == 'Barbara' or nome =='Manu':
    print('Belo nome feminino!')
else:
    print('Seu nome e bem normal!')
print(f'tenha um bom dia {nome}!')               

