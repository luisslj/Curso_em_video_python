def inteiro_para_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

# Exemplo de uso:
#num = int(input("Digite um número inteiro: "))
#print("O número em binário é:", inteiro_para_binario(num))


def inteiro_para_octal(numero):
    if numero == 0:
        return "0"
    octal = ""
    while numero > 0:
        octal = str(numero % 8) + octal
        numero = numero // 8
    return octal

# Exemplo de uso:
#num = int(input("Digite um número inteiro: "))
#print("O número em octal é:", inteiro_para_octal(num))


def inteiro_para_hexadecimal(numero):
    if numero == 0:
        return "0"
    hex_digitos = "0123456789ABCDEF"
    hexadecimal = ""
    while numero > 0:
        resto = numero % 16
        hexadecimal = hex_digitos[resto] + hexadecimal
        numero = numero // 16
    return hexadecimal

# Exemplo de uso:
#num = int(input("Digite um número inteiro: "))
#print("O número em hexadecimal é:", inteiro_para_hexadecimal(num))