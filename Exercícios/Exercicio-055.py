'''Faça um programa que leia o peso de cinco pessoas .
no final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor = 0


for i in range(1,6):
    peso = float (input(f'o peso da {i}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso    

print(f'O maior peso é {maior}!')
print(f'O menor peso é {menor}!')