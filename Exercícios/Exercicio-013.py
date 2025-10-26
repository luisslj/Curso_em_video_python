''' Faça um algoritimo que leia 
o salario de um fumcionario 
e mostre seu novo salário com 15% de aumento
'''

valor_salario = float(input('Digite o seu salario! R$ '))

aumento = (valor_salario /100)*15

novo_salario = valor_salario + (valor_salario*15/100)

#novo_salario = valor_salario + aumento

print(f'O valor do seu salário com aumento e de R$ {novo_salario}!')