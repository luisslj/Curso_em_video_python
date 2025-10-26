'''Desenvolva um programa que pergunte a distancia
de uma viagem em km calcule o preço da passagem,cobrando
R$0,50 por km para viagens se até 200km e 0,45 para mais longas.'''

viagem = float(input('Digite a distancia da viagem! '))

tax1 = 0.50
tax2 = 0.45

#preço = distancia * tax1 if distancia <= 200 else distancia * tax2

if viagem < 200:
    print(f'O valor da viagem e {viagem * tax1}')
else:
    print(f'o valor da viagem e {viagem*tax2}')    