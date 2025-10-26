galera =  list()
dado = list()
totmai = totmen = 0 
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()


for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai
    else:
        print(f'{p[0]} é menor de idade.')
        totmen

print(f'Temos {totmai} maiores e {totmen} menores de idade.')


teste = list() # O list() Serve para criar listas 
teste.append('Gusavo')
teste.append(40)
galeta = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
