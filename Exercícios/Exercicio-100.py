'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas 
funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai 
colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.'''


import random





def sorteia():
    lista = []
    cont = 0
    while cont < 5:
        cont += 1
        num = random.randint(1,9)
        lista.append(num)
    return lista    

def somapar(num):
    soma = 0
    for i in (num):
        if i % 2 == 0:
            soma += i
    return soma        


#Programa principal
sort = sorteia()
par = somapar(sort)

print(sort)
print(par)



