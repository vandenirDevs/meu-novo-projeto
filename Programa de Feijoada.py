#----------COMEÇO VOLUMEFEIJOADA--------
def volumeFeijoada():
    while True:
        try:
            print('Menu Volume Feijoada:')
            volume = int(input('Entre com o volume desejado (300ml a 5000ml): '))
            if 300 <= volume <= 5000:
                volume = volume * 0.08
                return volume

            else:
                print('Não aceitamos valores menores do que 300ml ou maiores do que 5L. Tente novamente: ')
                continue
        except ValueError:
            print('Você digitou um caractere não númerico. Tente de novo.')
            continue
    #----------FIM VOLUMEFEIJOADA----------

#----------COMEÇO OPCAOFEIJOADA--------
def opcaoFeijoada():
    while True:
        print('Menu Opção Feijoada:')
        opcao = input('Entre com a opção de feijoada: \n'
                          'B - Básica ( Feijão + Paiol + Costelinha) \n'
                          'P - Premium ( Feijão + Paiol + Costelinha + Partes de porco) \n'
                          'S - Suprema ( Feijão + Paiol + Costelinha + Partes de porco + Charque + Calabresa + Bacon)').upper()
        if opcao == 'B':
            return 1.00
        elif opcao == 'P':
            return 1.25
        elif opcao == 'S':
            return 1.50
        else:
            print('Opção inválida. Tente outra opção: ')
            continue
#----------FIM OPCAOFEIJOADA----------

#----------COMEÇO ACOMPANHAMENTOFEIJOADA--------
def acompanhamentoFeijoada():
    global valor
    while True:
        acompanhamento= int(input('Deseja mais algum acompanhamento: \n'
              '0 - Encerrar Pedido \n'
              '1 - 200g de arroz \n'
              '2 - 150g de farofa especial \n'
              '3 - 100g de couve cozida \n'
              '4 - 1 laranja descascada \n'))
        if acompanhamento == 0:
            return valor
        elif acompanhamento == 1:
            valor += 5
        elif acompanhamento == 2:
            valor += 6
        elif acompanhamento == 3:
            valor +=7
        elif acompanhamento == 4:
            valor += 3
        else:
            print('Opção inválida. Digite um número de acompanhamento ou 0 para sair: ')
            continue
#----------FIM ACOMPANHAMENTOFEIJOADA----------

#----------COMEÇO MAIN--------
volume = 0
valor = 0
opcao = ' '
print('Bem vindo ao menu de Feijoada do Vandenir Ferreira Jacques!!!')
volumeF = volumeFeijoada()
opcaoF = opcaoFeijoada()
acompanhamentoF = acompanhamentoFeijoada()
print('O valor total a ser pago é de R${:.2f} (volume = {} * opção = {} + acompanhamento = {})'.format(((volumeF * opcaoF) + acompanhamentoF), volumeF, opcaoF, acompanhamentoF))
#----------FIM MAIN----------



