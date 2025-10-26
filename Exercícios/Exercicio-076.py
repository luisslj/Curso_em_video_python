'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
 e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
 organizando os dados em forma tabular.'''


tupla = ('Pão',1,
         'Carne',22.90,
         'Queijo',44.90,
         'Presunto',22.2,
         'Morango',10.50)
print('-'*50)
print(' LISTA DE PREÇOS '.center(50))
print('-'*50)
for c in range(0,len(tupla),2):
    print(tupla[c],'.'*(39-len(tupla[c])),'R$','{:6.2f}'.format(tupla[c+1]))
print('-'*50)


# Lista de produtos e preços em uma tupla única
produtos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

# Cabeçalho
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Exibição tabular dos produtos e preços
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:<30} R$ {preco:>7.2f}')

print('-' * 40)



