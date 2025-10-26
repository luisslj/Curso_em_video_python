'''Crie um programa que leia um frase qualquer e diga se ela
é um palindromo desconsiderando os espaços.'''
#Ex:
#APOS A SOPA
#A SACASA DA CASA
#O LOBO AMA O BOLO
#ANOTRARAM A DATA DA MARATONA

frase = str (input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('E um palintromo')
else:
    print('não e um palintromo')    
print(junto, inverso)    

