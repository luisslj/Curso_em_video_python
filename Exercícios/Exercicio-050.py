'''Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares.Se o valor
digitado for impar, desconsidere-o'''
#10 % 2 != 0 impar
#10 % 2 == 0 par

s = 0
c = 0

for c in range(1, 7):
    num = int(input(f'Digite seis números {c} intero: '))
    s += num
    
    if num % 2 == 0:
       s += num 
       c += 1
    
print(f'os números pares são {c} a soma dos números pares é {s}.')