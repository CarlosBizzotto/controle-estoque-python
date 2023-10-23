# DEFINIÇÃO DE FUNÇÕES

# MOSTRA NO CONSOLE OS DADOS DE UMA UNICA PEÇA
def mostrarPeca(peca):
    print('Peça: || ' + 'Código: {}, Nome: {}, Fabricante: {}, Preço: {}'.format(peca['codigo'], peca['nome'], peca['fabricante'], peca['valor']) + ' ||')

# FAZ A BUSCA DE UMA DETERMINADA PEÇA DENTRO DA LISTA, POIS O ALGORITIMO É O MESMO PARA BUSCAS POR FABRICANTE E CÓDIGO
def verificarPeca(opcao, pecas):
    valor = input('Digite o ' + opcao + ' a ser procurado: ')
    encontrou = False

    for peca in pecas:
        if str(peca[opcao]) == valor:
            encontrou = True
            mostrarPeca(peca)

    if not encontrou:
        print('Peça não encontrada!')

# FAZ O CADASTRO DE UMA PEÇA NA LISTA
def cadastrarPeca(codigo):
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o fabricante da peça: ')
    valor = float(input('Digite o valor da peça: '))

    print('Peça cadastrada com sucesso!!')

    return {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}

# FAZ O CONTROLE DE BUSCA DE PEÇAS DE ACORDO COM O TIPO DETERMINADO
def consultarPeca(pecas):
    print('|| ' + 30 * '-' + ' ||')
    print('1. Consultar todas as peças')
    print('2. Consultar peças por codigo')
    print('3. Consultar peças por fabricante')
    print('4. Retornar')
    print('|| ' + 30 * '-' + ' ||')

    while True:
        opcao = int(input('Escolha o que você quer consultar: '))

        if opcao == 1:
            if len(pecas) > 0:
                print('|| ' + 30 * '-' + ' ||')
                for peca in pecas:
                    mostrarPeca(peca)
                print('|| ' + 30 * '-' + ' ||')
            else:
                print('Nenhuma peça cadastrada!')
        elif opcao == 2:
            verificarPeca('codigo', pecas)
        elif opcao == 3:
            verificarPeca('fabricante', pecas)
        elif opcao == 4:
            print('Retornando...')
            break
        else:
            print('Opção invalida! Tente novamente')

# REMOVE PEÇAS DA LISTA DE ACORDO COM O CÓDIGO
def removerPeca(pecas):
    codigo = int(input('Insira o código da peça a ser removida: '))

    for peca in pecas:
        if peca['codigo'] == codigo:
            pecas.remove(peca)


# PROGRAMA PRINCIPAL

pecas = []

print('Bem vindo(a) ao Controle de Estoque de Bicicletaria do Carlos Alexandre Pliskieviski Bizzotto')

while True:
    print('|| ' + 30 * '-' + ' ||')
    print('1. Cadastrar peça')
    print('2. Consultar peça')
    print('3. Remover peça')
    print('4. Sair')
    print('|| ' + 30 * '-' + ' ||')

    opcao = int(input('Digite a sua opção: '))

    # OPÇÃO PARA CADASTRO
    if opcao == 1:
        codigo = 0
        if len(pecas) == 0:
            codigo = 1
        else:
            codigo = pecas[len(pecas) - 1]['codigo'] + 1
        pecas.append(cadastrarPeca(codigo))
    # OPÇÃO PARA CONSULTA
    elif opcao == 2:
        consultarPeca(pecas)
    # OPÇÃO PARA REMOÇÃO DE PEÇAS DA LISTA
    elif opcao == 3:
        removerPeca(pecas)
    # OPÇÃO PARA FINALIZAR O PROGRAMA
    elif opcao == 4:
        print('Finalizando o programa...')
        break
    else:
        print('Codigo invalido!')
        print('Por favor tente novamente!')
        continue
