def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
           print(f'ERRO: \"{entrada}\" é um preço inválido!')
        else:
           valido = True
           return float(entrada)   
        

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor        
