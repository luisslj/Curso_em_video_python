'''Crie um programa que leia vários números inteiros pelo teclado.O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de perada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''

num = 0
soma = 0
cont = 0
while True:
    num = int (input('Digite um valor (999 para parar): '))
    cont += 1
    
    if num == 999:
        break
    soma += num


print(f'A soma dos {cont} valores foi {soma}')