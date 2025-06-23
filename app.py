# 📌 Observações importantes 

#O \n é para pular uma linha no terminal e também podemos usar aspas triplas
# Assim como o javaScript, podemos usar 'aspas simples' ou "aspas duplas"
# é possivel importar novas bibliotecas no pyhton usando o comando "import"
# def é para criar uma função no python
# Listas: [] → Ex: lista = [1, 2, 3]
# a escolha entre for e while dependerá da natureza específica do problema que você está resolvendo
#dicionarios = [{}, {}, {}], lista de dicionários: [{'nome': 'X', 'categoria': 'Y', 'ativo': False}, ...]
#.append() serve para adicionar algo a uma lista
# .ljust(n) alinha o texto
# os.system('cls') limpa a tela no terminal (Windows)
# if/elif/else são estruturas condicionais
# exit() encerra o programa imediatamente

import os

restaurantes = []

def exibir_nome_do_programa():
    #docstring
    '''Exibe o nome do programa na tela'''
    print("""
Sabor EXpress
          
""")

def exibir_opcoes():
    '''Exibe as opções disponíveis no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal'''
    input('\nAperte uma tecla para voltar ao menu principal. ')
    main()

def exibir_subtitulo(texto):
    '''Exibe um subtitulo na tela'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    '''Exibe uma mensagem de finalização do app'''
    exibir_subtitulo('Encerrando o programa.')
    
def opcao_invalida():
    '''Exibe um print de opção inválida e volta ao menu principal'''
    print('Opção inválida!')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar novos restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes.')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante ={'nome' : nome_do_restaurante, 'categoria' : categoria, 'ativo':False}
    #.append serve para adicionar algo a uma lista
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi adicionado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Listagem dos restaurantes
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    
    '''
    exibir_subtitulo('Listando restaurantes.')
    #para cada restaurante na lista restaurantes:
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    print("-" * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'inativo'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Alterna o status do restaurante para 'ativo' ou 'inativo'  
    
    Outputs: 
    - Exibe uma mensagem indicando o sucesso da operação

    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: opcao_invalida()
    except: opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main() 