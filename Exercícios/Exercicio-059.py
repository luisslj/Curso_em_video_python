'''Crie um programa que leia dois valores e mostre 
um menu na tela:'''
#[1]Somar
#[2]multiplicar
#[3]maior
#[4]novo número
#[5]Sair do programa
'''Seu programa deverá realizar a operação solicitada em cada caso.'''

print('Calculadora')
print('-='*25)
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor:'))
menu = 10
somar = valor1 + valor2
mult = valor1 * valor2
maior = valor1 / valor2
novo = valor1

while menu != 5:
    print('-'*25)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novo número')
    print('[5] Sair do programa')
    print('-'*25)
    menu = int(input('Escolha uma opção de 1 a 5: '))
    print('-'*25)
    if menu == 1:
        print('-'*25)
        print(f'A soma dos dois números e {somar}!')
    elif menu == 2:
        print('-'*25)
        print(f'A multiplicação dos dois números e {mult}!')  
    elif menu == 3:
        if valor1 > valor2:
            maior = valor1
        elif valor2 >valor1:
            maior = valor2
        else:
            print('Os dois números são iguais:')    
        print(f'Entre {valor1} e {valor2} o maior valor é {maior}')    
    elif menu == 4:
        print('Informe os números novamente')
        valor1 = float(input('Digite um valor: '))
        valor2 = float(input('Digite outro valor:'))
          
    elif menu == 5:
        print('Sair do programa')
            