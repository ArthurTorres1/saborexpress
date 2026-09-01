import os

restaurantes = ['Pizza Torres', 'Churrascaria do Zé', 'Sushi House', 'Hamburgueria do João']

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

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal...')
    main()

def cadastrarNovoRestaurante():
    os.system('cls')
    print('Cadastro de novo Restaurante\n')

    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')

    input('Pressione Enter para voltar ao menu principal...')
    main()

def listarRestaurantes():
    os.system('cls')
    print('Listagem de Restaurantes\n')

    for restaurante in restaurantes:
        print(f'- {restaurante}')
    
    input('\nPressione Enter para voltar ao menu principal...')
    main()

def escolher_opcao():
    try:
        opcao_escolha = int(input('Escolha uma opção: ' ))
        print(f'Você escolheu a opçao {opcao_escolha}\n')

        if opcao_escolha == 1:
            cadastrarNovoRestaurante()
        elif opcao_escolha == 2:
            listarRestaurantes()
        elif opcao_escolha == 3:
            print('Ativar Restaurante')
        elif opcao_escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()