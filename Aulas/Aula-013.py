#Curso Python #013 - Estrutura de repetição for

for c in range(0, 7, 2):
    print(c)
print('Fim')    

n = int(input('Digite um número!'))

for c in range(0, n+1):
    print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')        

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s = + n
print(f'A somatoria de todos os valores foi {s}')    