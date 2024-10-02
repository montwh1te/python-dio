from datetime import date, datetime, timedelta, timezone

LIMITE_SAQUES = 5
LIMITE_TRANSACAO = 10 
numero_saques = 0  
numero_transacao = 0  

saldo = 0
limite = 500
extrato = ""
pattern_format = "%d/%m/%Y %H:%M:%S"
dia_atual = (date.today().day + 1)
opcao = ''

print(f'''
      
********** Menu **********
      
      [1] Depositar
      [2] Sacar
      [3] Consultar extrato
      [4] Sair
      
      ''')

while opcao != 4:
    opcao = str(input('Selecione a sua opção: '))   
    match opcao:
        case '1':
            if (numero_transacao >= LIMITE_TRANSACAO):
                print('Você atingiu o número de transações diárias. (Atual: 10)')
            else:
                deposito = float(input('Digite o quanto você deseja depositar: '))
                saldo += deposito
                extrato += f'Depósito: R${deposito:.2f} | Data e Horário da transação: {(datetime.now(timezone(timedelta(hours=-3), "BRA-SUL"))).strftime(pattern_format)}\n'
                numero_transacao += 1
        case '2':
            if (numero_transacao >= LIMITE_TRANSACAO):
                print('Você atingiu o número de transações diárias. (Atual: 10)')
            elif (numero_saques >= LIMITE_SAQUES):
                print('Você atingiu o número de saques diários. (Atual: 5)')
            else:
                saque = float(input('Digite o quanto você deseja sacar: '))
                if (saque > limite):
                    print('Você ultrapassou o valor máximo de saque.')
                else:
                    saldo -= saque
                    extrato += f'Saque: R${saque:.2f} | Data e Horário da transação: {(datetime.now(timezone(timedelta(hours=-3), "BRA-SUL"))).strftime(pattern_format)}\n'
                    numero_saques += 1
                    numero_transacao += 1
        case '3':
            print('\n', ' Extrato '.center(17, '*'), '\n')
            print(extrato)
        case '4':
            break
           
    data_atual = date.today() 
    if (data_atual.day == (dia_atual)):
        dia_atual = date.today() + 1 
        numero_saques = 0
        numero_transacao = 0