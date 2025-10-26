'''Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:'''
#Média abaixo de 5.0:REPROVADO
#Média entre 5.0 e 6.9:RECUPERAÇÃO
#Média 7.0 ou superior:APROVADO

m1 = float(input('Digite a sua nota! '))
m2 = float(input('Digite outra nota! '))

media = (m1 + m2) / 2

if media < 5.0:
    print(f'Sua media e {media} está REPROVADO!')
elif 7 > media >= 5.0 and media < 7.0:
    print(f'Sua media e {media} esté em RECUPERAÇÃO')
elif media > 6.9 and media < 10.0:
    print(f'Sua media {media} está APROVADO')
elif media == 10:
    print(f'sua media e {media} PARABÉS TIROU A NOTA MAXIMA')    