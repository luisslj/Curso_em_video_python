def aumentar(num, t = 10):
    por = (num / 100) * t
    resultado = num + por
    return resultado

def diminuir(num, t = 10):
    por = (num /100) * t
    resultado = num - por
    return resultado

def metade(num):
    resultado = num / 2 
    return resultado

def dobro(num):
    resultado = num * 2
    resultado.split()
    return resultado

def moeda(preço =0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')