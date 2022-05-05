from abc import ABC, abstractmethod

'''DEFINIR A REGRAS PARA DUAS OPCOES DE CONTAS DISPONIVEIS'''


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia} ',
              f'Conta: {self.numero_conta}',
              f'Saldo: {self.saldo}')

    '''METODO OBRIGADO PARA AS CONTAS'''
    @abstractmethod
    def sacar(self, valor):
        pass


'''CLASSE PARA DEPOSITO E SAQUE SEM LIMITE DISPONIVEL'''


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()


'''CLASSE PARA DEPOSITO E SAQUE COM LIMITE DISPONIVEL'''


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite=100):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
