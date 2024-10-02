def deposito(valor, saldo, extrato):
    saldo += valor
    extrato += f'Depósito: R${valor:.2f}\n'
    return saldo, extrato
    
def saque(valor, num_saque, lim_saque, * , saldo, extrato):
    if (num_saque >= lim_saque):
        print('Você atingiu o número de saques diários. (Atual: 3)')
    elif (valor > limite):
        print('Você ultrapassou o valor máximo de saque.')
    else:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        num_saque += 1
    return saldo, extrato, num_saque
    
def mostrar_extrato(extrato):
    print(' Extrato '.center(17, '*'))
    print(extrato)
    
    
LIMITE_SAQUES = 3
numero_saques = 0    
saldo = 0
limite = 500
extrato = ""

saldo, extrato = deposito(1000, saldo, extrato)
saldo, extrato = deposito(100, saldo, extrato)
saldo, extrato, numero_saques = saque(100, numero_saques, LIMITE_SAQUES, saldo=saldo, extrato=extrato)
saldo, extrato, numero_saques = saque(200, numero_saques, LIMITE_SAQUES, saldo=saldo, extrato=extrato)
saldo, extrato, numero_saques = saque(300, numero_saques, LIMITE_SAQUES, saldo=saldo, extrato=extrato)
saldo, extrato, numero_saques = saque(100, numero_saques, LIMITE_SAQUES, saldo=saldo, extrato=extrato) # limite atingido aqui #
mostrar_extrato(extrato)

