'''Escreva um programa que pergunte o salário de um funcionario 
e calcule o valor do seu aumento.'''
#para salário superior a R$1.250, cacule um aumento de 10%.
#para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o seu salario? '))

if salario <=1250:
    novo = salario + (salario * 15 / 100)
    print(f'Quem ganhava R${salario:0.2f} passa a ganhar R${novo:0.2f} agora!')
else:
    novo = salario + (salario * 10 / 100)
    print(f'Quem ganhava R${salario:0.2f} passa a ganhar R${novo:0.2f} agora!')

