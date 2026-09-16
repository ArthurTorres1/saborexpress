import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
    {'nome': 'Feijoada do Torres', 'categoria': 'Brasileira', 'ativo': True}
    ]


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
    print('3-Alternar Estado de Restaurante (Ativar/Desativar)')
    print('4-Sair\n')

def finalizar_app():
    exibir_subtitulo('Saindo do programa...')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal... ')
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo) + 4)
    print(linha)
    print(subtitulo)
    print(linha)

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrarNovoRestaurante():
    exibir_subtitulo('Cadastro de Restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')

    dados_restaurante = {
        'nome': nome_restaurante,
        'categoria': categoria,
        'ativo': False
    }
    restaurantes.append(dados_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()

def listarRestaurantes():
    exibir_subtitulo('Listagem de Restaurantes')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternarEstadoRestaurante():
    exibir_subtitulo('Ativar/Desativar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso!\n' 
                if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!\n'
            )

            print(mensagem)
            break

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!\n')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolha = int(input('Escolha uma opção: ' ))
        print(f'Você escolheu a opçao {opcao_escolha}\n')

        if opcao_escolha == 1:
            cadastrarNovoRestaurante()
        elif opcao_escolha == 2:
            listarRestaurantes()
        elif opcao_escolha == 3:
            alternarEstadoRestaurante()
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