import random as rd

def gerador_numero_de_conta():
    numero_conta = ''.join([str(rd.randint(0, 9)) for _ in range(10)])
    return numero_conta 

class Conta_Bancaria:
    def __init__(self, num_conta, saldo, extrato, limite_saque_diario, proprietario):
        self.num_conta = num_conta
        self.saldo = saldo
        self.extrato = extrato
        self.limite_saque_diario = limite_saque_diario
        self.proprietario = proprietario
    def depositar(self):
        deposito = float(input('Digite o quanto você deseja depositar: '))
        self.saldo += deposito
        self.extrato += f'Depósito: R${deposito:.2f}\n'
    def sacar(self):    
        if (self.limite_saque_diario >= 3):
            print('Você atingiu o número de saques diários. (Atual: 3)')
        else:
            saque = float(input('Digite o quanto você deseja sacar: '))
            if (saque > 500):
                print('Você ultrapassou o valor máximo de saque.')
            else:
                self.saldo -= saque
                self.extrato += f'Saque: R${saque:.2f}\n'
                self.limite_saque_diario += 1
    def consultar_extrato(self):
        print(' Extrato '.center(17, '*'))
        print(self.extrato) 
    def informacoes_da_conta(self):
        print(f'''
              
Proprietário da conta: {self.proprietario.nome}         
CPF do Proprietário da conta: {self.proprietario.cpf}         
Número da conta: {self.num_conta}    
Saldo da conta: {self.saldo}      
              
              ''')     
        
class Proprietarios:
    def __init__(self, nome, cpf, data_de_nascimento, genero):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.genero = genero
    def listar(self):
        print(f'''
              
Nome: {self.nome}
CPF: {self.cpf}
Data de Nascimento: {self.data_de_nascimento}
Gênero: {self.genero}
              
              ''')
        
proprietario1 = Proprietarios('Eduardo', '023.432.321-53', '06/02/2003', 'M')
proprietario2 = Proprietarios('Roberto', '022.232.551-55', '06/02/2002', 'M')
proprietario3 = Proprietarios('Julio', '020.112.671-56', '06/02/2001', 'M')

conta1 = Conta_Bancaria(gerador_numero_de_conta(), 1230.00, '', 0, proprietario1)
conta2 = Conta_Bancaria(gerador_numero_de_conta(), 1000.00, '', 0, proprietario2)
conta3 = Conta_Bancaria(gerador_numero_de_conta(), 530.00, '', 0, proprietario3)

# Chamar as funções conforme o desejado
# conta1.depositar()
# conta1.depositar()
# conta1.depositar()
# conta1.sacar()
# conta1.sacar()
# conta1.sacar()
# conta1.sacar()
# conta1.sacar()
# conta1.consultar_extrato()
# conta1.informacoes_da_conta()
# conta2.consultar_extrato()
# conta2.informacoes_da_conta()