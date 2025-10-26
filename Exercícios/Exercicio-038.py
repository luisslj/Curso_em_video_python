'''Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:'''
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior,os dois são iguias 

num1 = int (input('Digite um número! '))
num2 = int (input('Digite outro número! '))

if num1 > num2:
    print (f'O primeiro número e maior {num1}!')
elif num2 > num1:
    print (f'O segundo numero e maior {num2}')
elif num1 == num2:
    print(f'Os dois numeros são iguais {num1} e {num2}!')        