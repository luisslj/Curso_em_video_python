'''Crie um programa que faça o controle de peças em uma produção de ferramentaria.'''


# Cadastro de peça 
# Cadastro de Operador
# Cadastro de maquina 
# Cadastro de Ordem de serviso
# Cadastro de Posição 

import json
import os



class Peca:
    def __init__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao

class Operador:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Maquina:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo

class OrdemServico:
    def __init__(self, numero, peca, operador, maquina, status):
        self.numero = numero
        self.peca = peca
        self.operador = operador
        self.maquina = maquina
        self.status = status

class Posicao:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao


# Exemplos de cadastro
pecas = []
operadores = []
maquinas = []
ordens_servico = []
posicoes = []

# Funções para cadastro
def cadastrar_peca(codigo, descricao):
    peca = Peca(codigo, descricao)
    pecas.append(peca)

def cadastrar_operador(nome, matricula):
    operador = Operador(nome, matricula)
    operadores.append(operador)

def cadastrar_maquina(numero, tipo):
    maquina = Maquina(numero, tipo)
    maquinas.append(maquina)

def cadastrar_ordem_servico(numero, peca, operador, maquina, status):
    ordem = OrdemServico(numero, peca, operador, maquina, status)
    ordens_servico.append(ordem)

def cadastrar_posicao(nome, localizacao):
    posicao = Posicao(nome, localizacao)
    posicoes.append(posicao)


def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Peça")
        print("2. Cadastrar Operador")
        print("3. Cadastrar Máquina")
        print("4. Cadastrar Ordem de Serviço")
        print("5. Cadastrar Posição")
        print("6. Listar Cadastros")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            codigo = input("Código da peça: ")
            descricao = input("Descrição da peça: ")
            cadastrar_peca(codigo, descricao)

        elif escolha == "2":
            nome = input("Nome do operador: ")
            matricula = input("Matrícula: ")
            cadastrar_operador(nome, matricula)

        elif escolha == "3":
            numero = input("Número da máquina: ")
            tipo = input("Tipo da máquina: ")
            cadastrar_maquina(numero, tipo)

        elif escolha == "4":
            numero_ordem = input("Número da ordem: ")
            codigo_peca = input("Código da peça: ")
            matricula_operador = input("Matrícula do operador: ")
            numero_maquina = input("Número da máquina: ")
            status = input("Status da ordem: ")

            # Procurando referências nos cadastros
            peca = next((p for p in pecas if p.codigo == codigo_peca), None)
            operador = next((o for o in operadores if o.matricula == matricula_operador), None)
            maquina = next((m for m in maquinas if m.numero == numero_maquina), None)

            if peca and operador and maquina:
                cadastrar_ordem_servico(numero_ordem, peca, operador, maquina, status)
            else:
                print("Erro: Verifique se a peça, operador e máquina estão cadastrados.")

        elif escolha == "5":
            nome = input("Nome da posição: ")
            localizacao = input("Localização: ")
            cadastrar_posicao(nome, localizacao)

        elif escolha == "6":
            print(f"\nPeças: {[p.descricao for p in pecas]}")
            print(f"Operadores: {[o.nome for o in operadores]}")
            print(f"Máquinas: {[m.numero for m in maquinas]}")
            print(f"Ordem de Serviço: {[o.numero for o in ordens_servico]}")
            print(f"Posições: {[p.nome for p in posicoes]}")

        elif escolha == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")
def salvar_dados():
    with open("dados.json", "w", encoding="utf-8") as f:
        json.dump({
            "pecas": [vars(p) for p in pecas],
            "operadores": [vars(o) for o in operadores],
            "maquinas": [vars(m) for m in maquinas],
            "ordens_servico": [vars(o) for o in ordens_servico],
            "posicoes": [vars(p) for p in posicoes]
        }, f, ensure_ascii=False, indent=4)

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            for p in dados["pecas"]:
                pecas.append(Peca(**p))
            for o in dados["operadores"]:
                operadores.append(Operador(**o))
            for m in dados["maquinas"]:
                maquinas.append(Maquina(**m))
            for o in dados["ordens_servico"]:
                peca = next((p for p in pecas if p.codigo == o["peca"]["codigo"]), None)
                operador = next((op for op in operadores if op.matricula == o["operador"]["matricula"]), None)
                maquina = next((mq for mq in maquinas if mq.numero == o["maquina"]["numero"]), None)
                ordens_servico.append(OrdemServico(o["numero"], peca, operador, maquina, o["status"]))
            for p in dados["posicoes"]:
                posicoes.append(Posicao(**p))
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    menu_principal()
