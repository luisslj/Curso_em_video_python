def aumentar(num, t = 10, formato = False):
    por = (num / 100) * t
    resultado = num + por
    return resultado if formato is False else moeda(resultado)

def diminuir(num, t = 10, formato =False):
    por = (num /100) * t
    resultado = num - por
    return resultado if formato is False else moeda(resultado)

def metade(num, formato=False):
    resultado = num / 2 
    return resultado if formato is False else moeda(resultado)

def dobro(num, formato=False):
    resultado = num * 2
    return resultado if formato is False else moeda(resultado)

def moeda(preço =0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(num,a=0,r=0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado:\t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num,True)} ')
    print(f'Metade do preço: \t{metade(num,True)}')
    print(f'{a}% de aumento: \t{aumentar(num,a,True)}')
    print(f'{r}% de redução: \t{diminuir(num,r,True)}')
    print('-' *35)

