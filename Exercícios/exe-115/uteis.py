

def titulo(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)

def menu():
   print('1 - Ver pessoas cadastradas')
   print('2 - Cadastrar nova Pessoa')
   print('3 - Sair do Sistema')
   print('-' *30)

def banco():# Criar o banco de dados se não existir
    dado = open('dados.txt', 'wt+')
    dado.close()

def bancoler():# ler o banco de dados 
    dado = open('dados.txt' , 'r')
    linhas = dado.readlines()
    for idx, linha in enumerate(linhas, start=1):
        linha = linha.strip()  # remove espaços e quebras de linha
        print(f"Item {idx}: {linha}")
        print("-" * 30)
        
    dado.close()



def bancoAdd():#Adicionar cadastro
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    dado = open('dados.txt' , 'a')
    dado.write(f'{nome},{idade}\n')
    dado.close()