# # DEFINIÇÃO DE FUNÇÕES
#
# #       RETORNA O DESCONTO EM RELAÇÃO AO VALOR TOTAL DA COMPRA
# def calcular_desconto(total, porcentagem):
#     # total = VALOR TOTAL DA COMPRA
#     # porcentagem = PORCENTAGEM DO DESCONTO
#     return (porcentagem * total) / 100
#
# #       MOSTRA OS RESULTADOS EM RELAÇÃO AOS VALORES INDICADOS
# def mostrar_resultados(qtd, valor, porcentagem = 0):
#     # qtd = QUANTIDADE DE PRODUTOS
#     # valor = VALOR DO PRODUTO
#     # porcentagem = PORCENTAGEM DO DESCONTO
#     if (qtd <= 9):
#         print('O valor total foi de: {:.2f}'.format(qtd * valor))
#     else:
#         total = qtd * valor
#         print('O valor total foi de: {:.2f}'.format(total))
#         print('O valor com desconto foi de: {:.2f} ({}% de desconto)'.format(total - calcular_desconto(total, porcentagem), porcentagem))
#
# # PROGRAMA PRINCIPAL
#
# print('Bem Vindo a Loja do Carlos Alexandre Pliskieviski Bizzotto')
#
# valor = float(input('Entre com o valor do produto: '))
# # qtd = QUANTIDADE DE PRODUTOS
# qtd = int(input('Entre com a quantidade do produto: '))
#
# # AQUI SÃO FEITAS AS VERIFICAÇÕES PARA O CALCULO DOS VALORES FINAIS DA COMPRA
#
# if (qtd <= 9):
#     mostrar_resultados(qtd, valor)
# elif ((qtd >= 10) and (qtd <= 99)):
#     mostrar_resultados(qtd, valor, 5)
# elif ((qtd >= 100) and (qtd <= 999)):
#     mostrar_resultados(qtd, valor, 10)
# elif (qtd >= 1000):
#     mostrar_resultados(qtd, valor, 15)

# exercicio 2 ------------------------------------------------------------------------------

# DECLARAÇÃO DE FUNÇÕES

#       RETORNA O VALOR DO PEDIDO EM RELAÇÃO AO SEU CODIGO
# def verificar_pedido(pedido):
#     if pedido == 100:
#         return 9.00
#     elif pedido == 101:
#         return 11.00
#     elif pedido == 102:
#         return 12.00
#     elif pedido == 103:
#         return 12.00
#     elif pedido == 104:
#         return 14.00
#     elif pedido == 105:
#         return 17.00
#     elif pedido == 200:
#         return 5.00
#     elif pedido == 201:
#         return 4.00
#     else:
#         return False
#
# # PROGRAMA PRINCIPAL
#
# # total = TOTAL A SER PAGO
# total = 0
# # verificador = VERIFICA SE O WHILE PRINCIPAL DEVE EXECUTAR
# verificador = True
#
# print('Bem vindo a Lanchonete do Carlos Alexandre Pliskieviski Bizzotto')
#
# while verificador:
#     pedido = int(input('Numero do pedido: '))
#     resultado = verificar_pedido(pedido)
#
#     if resultado != False:
#         total += resultado
#     else:
#         print('Codigo invalido, tente novamente!!')
#         continue
#
#     # ESSE LOOP VERIFICA SE O USUARIO QUER CONTINUAR A COMPRAR. ELE EXECUTA ENQUANTO NÃO FOR DIGITADO 'S' OU 'N'
#     while True:
#         continuar = input('Deseja fazer mais pedidos? [S/N]: ')
#
#         if continuar.upper() == 'S':
#             break
#         elif continuar.upper() == 'N':
#             print('Total a ser pago é: {:.2f}'.format(total))
#             verificador = False
#             break
#         else:
#             print('Opção invalida!!')
#             continue

# exercicio 3 -----------------------------------------------------------------------

# DEFINIÇÃO DE FUNÇÕES

# def dimensoesObjeto():
#     while True:
#         try:
#             altura = float(input('Qual a altura do objeto (em cm): '))
#             comprimento = float(input('Qual o comprimento do objeto (em cm): '))
#             largura = float(input('Qual a largura do objeto (em cm): '))
#         except:
#             print('Você digitou uma dimenção do objeto com valor não numérico')
#             print('Por favor entre com as dimenções desejadas novamente')
#             continue
#         else:
#             volume = altura * largura * comprimento
#
#             if volume < 1000:
#                 return 10
#                 break
#             elif volume >= 1000 and volume < 10000:
#                 return 20
#                 break
#             elif volume >= 10000 and volume < 30000:
#                 return 30
#                 break
#             elif volume >= 30000 and volume < 100000:
#                 return 50
#                 break
#             else:
#                 print('Não aceitamos objetos com dimensões tão grandes')
#                 print('Por favor entre com as dimenções desejadas novamente')
#                 continue
#
# def pesoObjeto():
#     while True:
#         try:
#             peso = float(input('Qual o peso do objeto (em KG): '))
#         except:
#             print('Você digitou um peso com valor não numérico')
#             print('Por favor entre com o peso desejado novamente')
#             continue
#         else:
#             if peso <= 0.1:
#                 return 1
#                 break
#             elif peso > 0.1 and peso < 1:
#                 return 1.5
#                 break
#             elif peso >= 1 and peso < 10:
#                 return 2
#                 break
#             elif peso >= 10 and peso < 30:
#                 return 3
#                 break
#             else:
#                 print('Não aceitamos objetos tão pesados')
#                 print('Por favor entre com o peso desejado novamente')
#                 continue
#
# def rotaObjeto():
#     while True:
#         rota = input('Qual a rota desejada: ')
#
#         if rota.upper() == 'RS':
#             return 1
#             break
#         elif rota.upper() == 'SR':
#             return 1
#             break
#         elif rota.upper() == 'BS':
#             return 1.2
#             break
#         elif rota.upper() == 'SB':
#             return 1.2
#             break
#         elif rota.upper() == 'BR':
#             return 1.5
#             break
#         elif rota.upper() == 'RB':
#             return 1.5
#             break
#         else:
#             print('Rota invalida!!')
#             print('Digite a rota desejada novamente!!')
#             continue
#
# # PROGRAMA PRINCIPAL
#
# print('Bem vindo(a) a Companhia de Logistica: Carlos Alexandre Pliskieviski Bizzotto')
#
# dimensoes = dimensoesObjeto()
# peso = pesoObjeto()
# rota = rotaObjeto()
#
# total = dimensoes * peso * rota
#
# print('Total a pagar: R${}, Dimensões: {} * Peso: {} * Rota: {}'.format(total, dimensoes, peso, rota))

# exercicio 4 --------------------------------------------------------------------------

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