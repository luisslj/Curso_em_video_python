#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.


# Exercício Python 106
# Mini sistema de ajuda interativo com cores

# Definindo cores ANSI
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m'
}

def titulo(msg, cor='branco'):
    print(cores[cor], end='')
    print('=' * (len(msg) + 4))
    print(f"  {msg}")
    print('=' * (len(msg) + 4))
    print(cores['limpa'], end='')

while True:
    titulo("Sistema de Ajuda PyHelp", 'verde')
    comando = input(f"{cores['amarelo']}Digite um comando (ou 'FIM' para sair): {cores['limpa']}")
    if comando.upper() == 'FIM':
        titulo("Encerrando... Até logo!", 'vermelho')
        break
    titulo(f"Acessando manual do comando '{comando}'", 'azul')
    help(comando)

