listaprodutos = []
#--------Início cadastrarprodutos-----------
def cadastrarProdutos(rp):
    print('Bem Vindo ao cadastro de produtos!')
    print('Código do Produto {}'.format(rp))
    nome = input('Digite o nome do produto: ')
    marca = input('Digite a marca do produto: ')
    valor = float(input('Digite o valor do produto: '))
    dicionarioProdutos = {'rp': rp,
                          'nome' : nome,
                          'marca' : marca,
                          'valor R$' : valor}
    listaprodutos.append(dicionarioProdutos.copy())
#--------Fim cadastrarprodutos-----------

#--------Início consultarprodutos-----------
def consultarProdutos():
    while True:
        try:
            print('Bem vindo ao consultar produtos: ')
            opcao = int(input('Digite a opção de consulta: \n'
                              '1 - Consultar todos os produtos \n'
                              '2 - Consultar Produto por código \n'
                              '3 - Consultar Produto(s) por fabricante \n'
                              '4 - Retornar \n'
                              '>> '))
            if opcao == 1:
                print('Consultar TODOS: ')
                for produto in listaprodutos:
                    for key, value in produto.items():
                        print('{} : {}'. format(key, value))
            elif opcao == 2:
                print('Consultar POR CÓDIGO: ')
                codigo = int(input('Digite o código do produto a ser consultado: '))
                for produto in listaprodutos:
                    if produto['rp'] == codigo:
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opcao == 3:
                print('Consultar POR FABRICANTE: ')
                fabricante = input('Digite o Fabricante a ser consultado: ')
                for produto in listaprodutos:
                    if produto['marca'] == fabricante:
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opcao == 4:
                print('Voltando ao menu anterior...')
                return
            else:
                print('Opção inválida')
        except ValueError:
            print('Você digitou algum caractere não especificado no MENU. Tente de novo.')
# --------Fim consultarprodutos-----------

# --------Início removerprodutos-----------
def removerProdutos():
    print('Bem vindo ao remover produtos.')
    remover = int(input('Digite o código do produto a ser removido: '))
    for produto in listaprodutos:
        if produto['rp'] == remover:
           listaprodutos.remove(produto)
# --------Fim removerprodutos-----------

#--------Início Main-----------
print('Bem Vindo ao programa de controle de estoque Vandenir Ferreira Jacques!')
registroProdutos = 0
while True:
    try:
        opcao = int(input('Digite a opção desejada: \n'
                          '1 - Cadastrar Produto \n'
                          '2 - Consultar Produto(s) \n'
                          '3 - Remover Produto \n'
                          '4 - Sair \n'
                          '>> '))
        if opcao == 1:
            registroProdutos += 1
            cadastrarProdutos(registroProdutos)
        elif opcao == 2:
            consultarProdutos()
        elif opcao == 3:
            removerProdutos()
        elif opcao == 4:
            print('Programa encerrado...')
            break
        else:
            print('Opção inválida. Tente de novo.')
    except ValueError:
        print('Você digitou um caractere não definido no Menu. Tente de novo.')
        continue
#--------Fim Main-----------


