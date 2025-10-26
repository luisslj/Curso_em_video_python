'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer 
mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos.'''


print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Digite o primeiro termo: '))#primeiro termo
razao = int(input('Digite a razão: '))#razão
termo = primeiro
cont = 1
total = 0 
mais = 10

while mais !=0:
    total = total + mais
    while cont != total:
        print(f'{termo}-',end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
 
   

print('FIM') 
print(f'Progreção finalizada com {total} termos mostrados.')