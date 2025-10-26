lanche = ('Hamburquer','Suco','Pizza','Pudim')
#tuplas são imutáveis

print(lanche)
print(lanche[0])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
print(len(lanche))
for cont in range(0, len(lanche)):
    print(cont)
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')   

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')    

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(c))#deixa em ordem alfa númerico
print(c.count(5))#conta a quantidade de itens iguais 
print(c.index(8))#em que posição esta o itens
print()