'''Crie um programa que leia vários números inteiros pelo 
teclado.No final da execução, mostre a média entre todos os 
valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar
os valores.'''

num = 0
menor = 0
maior = 0
cont = 0
media = 0
continuar = 's'
soma = 0

while continuar != 'N':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num            

media = soma / cont
    
print(f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}')









