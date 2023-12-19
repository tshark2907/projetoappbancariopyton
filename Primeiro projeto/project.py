saldo = 3000
opcao = int(input('Escolha uma opção:\n[1]Saque\n[2]Depósito\n[3]Extrato\n[4]Sair\n'))
limiteNumeroSaques = 3
limiteSaque = 500
operacoes = []

while(opcao != 4):
    
    if(opcao == 1):

        quantidade = int(input('Insira o valor a ser sacado:\n'))
        if(quantidade > limiteSaque):
            print('Seu limite de saque é de R$ '+str(limiteSaque)+' por saque, favor tentar um valor menor.\n')
        elif(limiteNumeroSaques > 0):
            saldo = saldo - quantidade
            limiteNumeroSaques -= 1
            print('Saldo atualizado: R$'+str(saldo)+'. Seu numero de saques restantes hoje é de '+str(limiteNumeroSaques)+' saques.\n')
            opcao = int(input('Escolha uma opção:\n[1]Saque\n[2]Depósito\n[3]Extrato\n[4]Sair\n'))
            operacoes.append('Saque: '+str(quantidade)+'R$.')
        else:
            print('Voce excedeu o limite de saques de hoje, tente novamente amanhã\n')
            
            opcao = int(input('Escolha uma opção:\n[1]Saque\n[2]Depósito\n[3]Extrato\n[4]Sair\n'))
    elif(opcao == 2):
        quantidade = int(input('Insira o valor que deve ser depositado:\n'))
        if(quantidade > 0):
            saldo = saldo + quantidade
            print('Saldo atualizado: R$ '+str(saldo)+'.\n')
            opcao = int(input('Escolha uma opção:\n[1]Saque\n[2]Depósito\n[3]Extrato\n[4]Sair\n'))
            operacoes.append('Deposito: '+str(quantidade)+'R$.')
    elif(opcao == 3):
        print('Saldo atual: '+str(saldo)+' R$.')
        print('Operacoes bancarias hoje:')
        nLinhas = len(operacoes)
        for linha in operacoes:
            print(linha)
        opcao = int(input('\nEscolha uma opção:\n[1]Saque\n[2]Depósito\n[3]Extrato\n[4]Sair\n'))
    elif(opcao ==  4):
        print('Muito obrigado por usar nosso banco, volte sempre!\n')
        