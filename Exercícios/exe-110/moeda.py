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