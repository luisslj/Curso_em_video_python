'''Escreva um programa que leia um número interiro 
qualquer e peça para o usuário escolher qual será a 
base de conversão'''
#-1 para binario
#-2 para octal
#-3 para hexadecimal

from teste import inteiro_para_binario, inteiro_para_hexadecimal,inteiro_para_octal

num = int(input('Digite um número inteiro! '))

print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
op = int (input ('Sua opção: '))

if op == 1:
    bine = inteiro_para_binario(num)
    print(f'{num} convertido para BINÁRIO é igual a {bin}'[2:])
elif op == 2:

    print(f'{num} convertido para OCTAL é igual a {oct}'[2:])

elif op == 3:

  print (f'{num} convertido para HEXADECIMAL é igual a {hex}')  
else:
   print('Opção invalida')       