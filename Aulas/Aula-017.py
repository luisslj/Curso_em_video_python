num = [2, 5, 9, 1]
num[2] = 3 # trocar um indice na lista 
num.append(7) # adicionar um item na lista 
num.sort # em orderm alfa numerico 
num.sort(reverse =True)# em ordem do maior para o menor 
num.insert(2, 0)# inserie um item na lista
num.pop()# numero sem parametro tira o ultimo item da lista 
num.remove(0)#elimina o item da lista selecionado podendo usar lop ou if
len(num)# para ler a quantidade de item na lista criada 
if 4 in num:
    num.remove(4)
else:
    print('não achei o nuemro 4.')    
print(num)
print(f'Essa lista tem {len(num)} elementos.')

from random import randint
valores = [] # ou list() para cria uma lista vazia 
valores.append(5)
valores.append(8)
valores.append(5)
valores.append(randint(1,10))
valores.append(randint(1,10))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')    
print(valores)

#lista com conexão uma com a a outra 
a =  [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# para cria um copia de um uma lista 
c =  [2, 3, 4, 7]
d = c[:]
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')
