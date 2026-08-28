import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 

""")

def exibir_opcoes():
    print('1-Cadastrar Restaurante')
    print('2-Listar Restaurantes')
    print('3-Ativar Restaurante')
    print('4-Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app...\n')
    exit()

def escolher_opcao():
    opcao_escolha = int(input('Escolha uma opção: ' ))
    print(f'Você escolheu a opçao {opcao_escolha}\n')

    if opcao_escolha == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolha == 2:
        print('Listar Restaurantes')
    elif opcao_escolha == 3:
        print('Ativar Restaurante')
    else:
        finalizar_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()