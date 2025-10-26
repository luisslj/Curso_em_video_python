from random import randint,choice
import time


senha = int(input('Digite uma senha: '))
computador = 0
contador = 0




while computador != senha:
    contador += 1
    print(contador)
    computador = randint(100,999)

print(senha)
print(computador)    