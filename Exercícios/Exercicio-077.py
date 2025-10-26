'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, 
quais são as suas vogais.'''


# Tupla com várias palavras (sem acentos)
palavras = ('aprender', 'programar', 'python', 'desenvolver', 'computador', 'teclado', 'mouse', 'internet')

# Para cada palavra, mostrar suas vogais
for palavra in palavras:
    print(f'\nNa palavra **{palavra.upper()}** temos:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
