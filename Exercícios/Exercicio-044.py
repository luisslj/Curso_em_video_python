'''Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e com a condição de pagamento:'''
'''- à vista dinheiro: 10% de desconto
-à vista no cartão:5% de desconto
-em até 2x no cartão:preço normal
-3x ou mais no cartão 20% de juros'''
print('-='*30)
preco = float(input('Digite o valor do produto:R$ '))
print('-='*30)
print('À vista dinheiro digite 1:')
print('À vista no cartão credito 2:')
print('Em até 2x no catão 3')
print('Em mais de 3x no cartão 4')
print('-='*30)
op = int(input('Digite a opção: '))
print('-='*30)

if op == 1:
    preco = preco-(preco * 10 / 100)
    print(f'O preço a vista fica R${preco}.')
elif op == 2:
    preco = preco - (preco * 5 / 100)
    print(f'O preço a vista no cartão fica R${preco}')
elif op ==3:
    preco
    print(f'O preço dividido em 2x e R${preco}')
elif op == 4:
    preco = preco + (preco * 20 / 100) 
    print(f'O preço dividido em mais vezes fica R${preco}')
else:
    preco = preco
    print('tente novamente')    

