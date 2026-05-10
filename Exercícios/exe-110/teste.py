import moeda


num = float(input('Digite um numero:'))

print(f'O aumento de {num} e {moeda.aumentar(num,10,True)}.')
print(f'O diminutivo de {num} e {moeda.diminuir(num,15,True)}.')
print(f'O dobro de {num} e {moeda.dobro(num,True)}.')
print(f'A metade de {num} e {moeda.metade(num,True)}.')