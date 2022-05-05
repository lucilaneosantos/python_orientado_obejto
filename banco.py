'''CLASSE RESPONSAVEL PELO ARMAZEMAMENTO E VALIDACAO DE SAQUE E DEPOSITO'''


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3323]
        self.contas = []
        self.clientes = []

    '''ADCIONA CLIENTE NO LISTA DO BANCO'''

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    '''ADCIONA CONTA NO LISTA DO BANCO'''

    def inserir_conta(self, conta):
        self.contas.append(conta)

    '''AUTENTICAÇÃO DE TRES ETAPAS, LISTA DE AGENCIA PRE-CADASTRADA NA INICIALIZACAO DA CLASSE'''

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        return True
