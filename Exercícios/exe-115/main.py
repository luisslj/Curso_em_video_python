import uteis 

opcao = 0

while True:
    uteis.titulo('MENU PRINCIPAL')
    uteis.menu()
    try:
        opcao = int(input('Sua Opção: '))
    except:
        print('Erro: por favor, digite um número inteiro válido.')    
    if opcao == 1:
        uteis.titulo('VER PESSOAS CADASTRADAS')
        uteis.bancoler()
        
    elif opcao == 2:
        uteis.titulo('CADASTRAR NOVA PESSOA')
        uteis.bancoAdd()
        print('2')
    elif opcao == 3:
        uteis.titulo('SAIR DO SISTEMA')
        break

