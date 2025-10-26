'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
num = 0
maior = 0
menor = 0

for i in range(0,5):
    lista.append(int(input('Digite um numero: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]    


lista.sort
print(max(lista))
print(lista)
for i,v in enumerate(lista):
    if maior in lista(v):
        print(i)
print(maior)
print(menor)

