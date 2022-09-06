print('Bem Vindo à Pizzaria do Vandenir Ferreira Jacques!')
print('-'*20,'CARDÁPIO', '-'*20)
print('| Código | Descrição | Pizza Média | Pizza Grande |',end='\n')
print('|   21   | Napolitana|    R$ 20,00 |     R$ 26,00 |',end='\n')
print('|   22   | Margherita|    R$ 20,00 |     R$ 26,00 |',end='\n')
print('|   23   | Calabresa |    R$ 25,00 |     R$ 32,00 |',end='\n')
print('|   24   | Toscana   |    R$ 30,00 |     R$ 39,00 |',end='\n')
print('|   25   | Portuguesa|    R$ 30,00 |     R$ 39,00 |',end='\n')

cont = 0
cont1 = 0
sabor = 0
valor = 0
conf = ' '
while True:
    tam = input('Qual o tamanho da pizza que deseja M, G? ').upper()
    while tam!= 'M' and tam != 'G':
        print('Opção inválida!')
        tam = input('Qual o  tamanho da pizza que deseja M, G? ').upper()

    while True:
        sabor = int(input('Digite o código sabor desejado: '))
        if sabor == 21:
            if tam == 'M':
                valor += 20
            else:
                valor += 26
            print('Você escolheu Napolitana.')
            break
        elif sabor == 22:
            if tam == 'M':
                valor += 20
            else:
                valor += 26
            print('Você escolheu Margherita.')
            break
        elif sabor == 23:
            if tam == 'M':
                valor += 25
            else:
                valor += 32
            print('Você escolheu Calabresa.')
            break
        elif sabor == 24:
            if tam == 'M':
                valor += 30
            else:
                valor += 39
            print('Você escolheu Toscana.')
            break
        elif sabor == 25:
            if tam == 'M':
                valor += 30
            else:
                valor += 39
            print('Você escolheu Portuguesa.')
            break
        else:
            print('Opção inválida!')
            continue
    conf = input('Deseja fazer outro pedido? (S/N): ').upper()
    if conf == 'S':
        continue
    else:
        print('Fechando pedido...')
        break
print('O valor total do pedido é R${:.2f}'.format(valor))

