LIMITE_SAQUES = 3
numero_saques = 0    
saldo = 0
limite = 500
extrato = ""

print(f'''
      
********** Menu **********
      
      [1] Depositar
      [2] Sacar
      [3] Consultar extrato
      [4] Sair
      
      ''')

opcao = ''

while opcao != 4:
    opcao = str(input('Selecione a sua opção: '))
    match opcao:
        case '1':
            deposito = float(input('Digite o quanto você deseja depositar: '))
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}\n'
        case '2':
            if (numero_saques >= LIMITE_SAQUES):
                print('Você atingiu o número de saques diários. (Atual: 3)')
            else:
                saque = float(input('Digite o quanto você deseja sacar: '))
                if (saque > limite):
                    print('Você ultrapassou o valor máximo de saque.')
                else:
                    saldo -= saque
                    extrato += f'Saque: R${saque:.2f}\n'
                    numero_saques += 1
        case '3':
            print(' Extrato '.center(17, '*'))
            print(extrato)
        case '4':
            break
        
        