nome = str(input('Qual é seu nome? ')).upper()
nome1 = 'GUSTAVO'

if nome == nome1:
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')


n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2

if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
