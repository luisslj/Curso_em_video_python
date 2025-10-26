# Programa para gerenciar o aproveitamento de um jogador de futebol

jogador = {}         # Dicionário para armazenar os dados do jogador
gols = []            # Lista para armazenar os gols por partida

# Entrada de dados
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Coleta de gols por partida
for i in range(partidas):
    gol = int(input(f'  Quantos gols na partida {i + 1}? '))
    gols.append(gol)

# Armazenando os dados no dicionário
jogador['gols'] = gols
jogador['total'] = sum(gols)

# Exibição dos dados
print('-=' * 30)
print(jogador)
print('-=' * 30)

# Detalhamento dos campos
for k, v in jogador.items():
    print(f'O campo "{k}" tem o valor {v}.')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

# Detalhamento por partida
for i, g in enumerate(jogador['gols']):
    print(f'  => Na partida {i + 1}, fez {g} gols.')

print(f'Foi um total de {jogador["total"]} gols.')