'''Escreva um programa que pergunte a quantidade de 
km percorrido por um carro alugado e a quantidade de dias
pelo quais ele foi alugado. calcule o preço a pagar, 
sabemos que o carro custa R$60 por dia e R$0,15 por km rodado.'''
print('-'*40)
dias = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quanto kilometros foi rodado? '))

valor_dia = dias * 60
valor_km = km * 0.15
valor_total = valor_dia + valor_km

print('-'*40)
print(f'O valor do KM rodado deu R${valor_km}!')
print(f'o valor da diaria deu R${valor_dia}!')
print(f'Valor total a pagar de R$ {valor_total}')
print('-'*40)
