'''Desnvolva um programa que leia o nome, idade e sexo
de 4 pessoas.No final do programa, mostre:'''
#A média de idade do grupo
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos 

somaidade = 0
medidaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulhe20 = 0
for i in range(1, 5):
    print(f'-----{i}°-----')
    nome = str (input('Digite seu nome: '))
    idade = int (input('Digite sua idade: '))
    sexo = str (input('Sexo [M/F]: '))
    somaidade = somaidade + idade
    if i ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totalmulhe20 +=1       

mediaidade = somaidade / i
print(f'A media de idade {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}!!!')
print(f'o total de mulheres com menos de e 20 são {totalmulhe20}')