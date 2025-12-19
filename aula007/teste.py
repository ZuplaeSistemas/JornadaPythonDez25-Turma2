from time import sleep

opcao = -1

while opcao != 0:
    print('='*20, 'Módulo Funcionário' ,'='*20, '\n')

    print('\t1-Cadastrar')
    print('\t2-Editar')
    print('\t3-Listar')
    print('\t4-Deletar')
    print('\t0-Sair')

    opcao = int(input('\n\tEscolha uma das opções:'))

    match opcao:
        case 0:
            print('Saindo ...')
        case 1:
            print('Cadastrando ...')
        case 2:
            print('Editando ...')
        case 3:
            print('Listando ...')
        case 4:
            print('Deletando ...')
        case _:
            print('Opcao invalida')
    
    sleep(3)