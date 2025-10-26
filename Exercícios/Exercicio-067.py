'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário, O programa será interrompido quando o número
solicitado for negativo.'''




num = 0
cont = 0

print('-'*30)
print('Taboada')


while True:
    print('-'*30)
    num = int(input('Quer ver a taboada de qual valor?  '))
    print('-'*30)
    if num < 0:
          break
    elif num > 1:
        for cont in range(1,11):
            print(f'{num} X {cont} = {num*cont}')
            cont += 1

    
    
      