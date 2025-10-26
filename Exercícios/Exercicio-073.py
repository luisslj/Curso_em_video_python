'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
 Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

times_brasileirao = (
    "Flamengo", "Cruzeiro", "Palmeiras", "Bahia", "Bragantino",
    "Botafogo", "Mirassol", "São Paulo", "Ceará", "Internacional",
    "Corinthians", "Fluminense", "Atlético-MG", "Grêmio", "Vitória",
    "Vasco", "Santos", "Fortaleza", "Juventude", "Sport"
)


cont = 0

ordem = (sorted(times_brasileirao)) #Times em ordem alfabética
'''while True:
    if times_brasileirao == "Ceará":
        cont+=1
        break'''

print(f'lista dos times Brasileiros {times_brasileirao}')
print('='*30)
print(F'Os 5 primeiros são {times_brasileirao[0:5]}')
print('='*30)
print(f'os 4 ultimos times {times_brasileirao[-4:]}')
print('='*30)
print(f'Times em orde alfabética: {ordem}')
print('='*30)
print(f'O bragantino está na {times_brasileirao.index("Bragantino")+1} posição')









