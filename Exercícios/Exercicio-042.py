'''Refaça o DESAFIO 035 dos triangulos acrescentado o 
recurso de mostrar que tipo de tringulo será formado:'''
# - Equilátero:todos os lados iguais
# - Isósceles:dois lados iguais
# - Escaleno:todos os lados doferentes

a = float(input('Digite a primeira reta! '))
b = float(input('Digite a segunda reta! '))
c = float(input('Digite a terceira reta! '))


if a + b > c and a + c > b and b + c > b:
    print(f'Pode formar um triangulo!')
else:
    print(f'Não pode formar um tringulo')

if  a == b == c :
    print('E um tringulo Equilátero') 
elif a == b or  a == c or   b == c:
    print('E um tringulo Isósceles')  
elif  a != b or b != a  or  a != c:
    print('e um triangulo Escaleno')