'''Um professor quer sortear um dos seus alunos
para apagar o quadro.Faça um programa que
ajude ele, lendo o nome deles e escrevendo o nome
do escolhido'''

'''import random
list = ['Luis','Pedro', 'Barbara']
nome = random.choice(list)
print(nome)'''

import random

n1 = str(input('Digite o primeiro nome! '))
n2 = str(input('Digite o segundo nome"! '))
n3 = str(input('Digite o terceiro nome! '))
n4 = str(input('Digite o quarto nome! '))
list = [n1, n2, n3, n4]
escolhido = random.choice(list)
print(f'O aluno escolhido foi {escolhido}!')