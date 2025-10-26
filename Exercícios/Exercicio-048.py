'''Faça um programa que calcule a soma entre todos os 
números impares que são multiplos de três e que se 
encontram no intervalo de 1 até 500.'''

n = 0
c = 0
for i in range(0, 500, 3):
     if i % 2 != 0:
          print(i)
          n += i
          c = c + 1

# i % 3 !=0 serve para ver se pode ser multiplo


print(f'A soma de todos os números inpar multiplo de três é {n}')
print(c)