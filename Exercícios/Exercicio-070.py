'''Crie um programa que leie o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar . No final, mostre:'''
#A) Qual è o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#c) Qual é o nome do produto mais barato.


produto = ''
preco = 0
cont = ''
total = 0
produto1 = 0 #produto mais de 1000 reias
produto2 = 0 #mais barato
preco1 = 0 #mais caro
preco2 = 0 #mais barato
n = 0
preco1000 = 0
produtob = ''

print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)


while True:
    produto = str (input('Nome do produto:'))
    preco = int (input('Digite o preço do produto R$: '))
    cont = str (input('Quer continuar? [S/N]'))
    while cont not in 'sn':
        cont = str (input('Quer continuar? [S/N]'))
    total += preco
    n += 1
    if n == 1:
        preco1 = preco2 = preco
    else:
        if preco > preco1:
           preco1 = preco
        if preco < preco2:
            produtob = produto 
    if preco >= 1000:
        preco1000 += 1

    if  cont == 'n':
        break
    



print('-----FIM-----')
print(f'Total da compra foi R${total}')#ok
print(f'Temos {preco1000} produtos custando mais de R$1000,00')#ok
print(f'O produto mais barato foi {produto}')
print(f'Preço mais caro {preco1}')





    
