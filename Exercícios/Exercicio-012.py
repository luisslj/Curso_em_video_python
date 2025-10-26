'''Faça um algoritimo que leia o preço
de um produto e mostre seu novo preço com 
5% de desconto
'''
preco = float(input('Digite o preço do produto! '))

valor_desconto = (preco /100)*5

novo = preco -(preco * 5 / 100)

#novo_preco = preco - valor_desconto

print(f'Preco do produto com desconto R${novo:0.3} !')

