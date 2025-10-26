'''Faça um programa que leia a largura
e a altura de uma parece em metros,
calcule a sua área e a quantidade de 
tinta necessária para pintá-la, sabendo 
que cada litro de tinta, pinta uma área de 2M²
'''

a = float(input('Qual a altura de uma parece? '))
l = float(input('Qual a largura da parede? '))
p = a * l
t = p / 2

print(f'A área da parece e {p}M²!')
print(f'são e preciso {t:0.3}l para pintar essa parece!')