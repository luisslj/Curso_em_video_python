'''Crie um programa que leia o nome de uma 
cidade e diga se ela começa ou não com 
o nome Santo.'''

'''cid = str(input('Em que cidade que você naceu? ')).strip()
print(cid[:5].upper() == 'SANTOS')'''

nome = str(input('Digite um nome qualquer!')).strip()

nome1  = "SANTOS"
nome = nome.split()


if nome1 in nome[0].upper():
    print(f'Tem {nome1} no primeiro nome')
else:
    print(f'Não tem {nome1} no primeiro nome')  


  