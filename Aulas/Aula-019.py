#Tuplas ()
#Lista []
#Dicionario{}

#print(filmes.values())
#print(filmes.keys())
#print(filmes.items())

dados = dict()
dados = {}
pessoa = {'nome':'Gustavo','sexo':'M','idade':22}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')
print(pessoa.keys())# Keys mostra as chaves 
print(pessoa.values())# Values mostras os valores 
print(pessoa.items())# mostra os itens 
for k in pessoa.keys():
    print(k)
for v in pessoa.values():
    print(v) 
pessoa ['nome'] = 'Leandro'# para trocar um itens de um dicionario
pessoa['peso'] = 98.5 # para adicionar um valor para a lista não precisa usar append     
for k, v in pessoa.items():# o items ser para usar no lugar do enumaretes
    print(f'{k} = {v}')
del pessoa['sexo'] #del serve para deletar um valor da lista 

brasil = []
estado1 = {'uf':'Rio deJaneiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])
print(brasil[0])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Silga do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()            










