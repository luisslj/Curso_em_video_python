'''Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar no final, mostrar:'''
#A) Quantas pessoas tem mais de 18 anos.
#b) Quantas homems foram cadastrados.
#c) Quantas mulheres  tem menos de 20 anos.




print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)

idade = 0
sexo = 'o' #[S/M]
cont = 's'
mulher20 = 0
homens = 0
pessoas18 = 0
n = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[F/M] '))
    while sexo not in 'mf':
        sexo = str(input('Sexo:[F/M] '))

    print('-'*30)
    cont = str(input('Quer continuar? [S/N]: '))
    while cont not in 'sn':
        cont = str(input('Quer continuar? [S/N]: '))
    print('-'*30)
    if sexo in 'Ff' and idade <= 20:
        mulher20 +=1 
    if  idade >= 18:
        pessoas18 +=1 
    if sexo in 'Mm':
        homens +=1         
    if cont == 's':
        print('CADASTRE UMA PESSOA')
        print('-'*30)
    if cont == 'n':
        break 
    n += 1
    


print('===== FIM DO PROGRAMA =====')
print(f'Total de {pessoas18} pessoas com mais de 18 anos')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
print(f'Foram cadastrado {homens} homens.')