# Modify Strings

txt = 'Luis Souza Jacinto'
t = str(input('Digite uma palavra! '))
L = str(input('Digite uma letra para trocar '))

if t in txt:
    print('Sim tem essa palavra')
else:
    print('Não tem essa palavra')

if t not in txt:
    print('não tem essa palavra! ')
else:
    print('tem essa palavra')    


print(txt[2:5])
print(txt[:5])  
print(txt[2:]) 
print(txt[-5:-2])
print(txt.upper())# Deixa todas as str maiusculas
print(txt.lower())# Deixa todas as str minusculas
print(txt.strip())# Remove espaço em branco no começo e no final da frase
print(txt.replace('L',L))# troca uma str por outra
print(txt.split('o'))# O split()método divide a string em substrings se encontrar instâncias do separador:

