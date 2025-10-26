frase='Curso em video Python'
frase1 = '   Aprenda Python   '


len(frase) #Ler o numero de carecteris 
frase.count('o') # contar quantas letras tem na str
frase.count('o',0,13)
frase.find('deo')# encontra a posição da frase  ()
frase.find('Android')# procura a palavra na frase e se não acha retorna -1
'Curso' in frase #verifica se tem essa palavra na frase
#Fatiar
print(len(frase))
print(frase.count('o'))
print(frase.count('o',13))
print(frase.find('deo'))
print(frase.find('Androd'))
print('Curso'in frase)
print(frase[3:13])
print(frase[3:])
print(frase[:3])
print(frase[::2]) #mostra pulando de 2 em 2
print(frase[2::])

#transformar
print(frase.replace('Python','Androd'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())# Deixa o começo de cada palavra minuscula pulando a primeira
print(frase.title())# Deixa o começo de todas as palavaras maiuscula
print(frase1.strip())# remove espaço em branco no começo e no final
print(frase1.rstrip())# romeve espaços vazio no final da frase
print(frase1.lstrip())# romove espaços vazio no começo da frase

#Divisão
print(frase.split())
print('-'.join(frase))

dividido = frase.split()
n1 = int(input('Digite o numero!'))
print(dividido[n1][3])