'''Exercicio com abstração, herança, encapsulamento e polimorfismo  
criar um sistema bancario(extremamente simples) que tem clientes, contas
e um banco. A ideia é que o cliente tenha uma conta(poupancça ou corrente) 
e que possa sacar/depositar nessa conta. Contas corrente tem um limite 
extra. Banco tem clientes e contas.'''
from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

'''INSTANCIAR BANCO PARA VALIDAÇÃO E POSIBILIDADE DE SAQUE OU DEPOSITO'''
banco = Banco()
# 1
cliente1 = Cliente('Luiz', 30)
# 2
cliente2 = Cliente('Lucas', 30)
# 3
cliente3 = Cliente('João', 30)

'''CRIACAO DA CONTA POR TIPO ESPECIFICO'''
# 1
conta1 = ContaPoupanca(1111, 254134, 0)
# 2
conta2 = ContaPoupanca(2222, 254224, 0)
# 3
conta3 = ContaCorrente(3323, 454134, 0)

'''CLIENTE RECEBE SUA CONTA DE CADASTRO'''
# 1
cliente1.inserir_conta(conta1)
# 2
cliente2.inserir_conta(conta2)
# 3
cliente3.inserir_conta(conta3)

'''INSERE CLIENTE NA LISTA DO BANCO'''
# 1
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
# 2
banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

''' VERIFICAR SE CLIENTE , CONTA E AGENCIA SÃO VALIDOS E REALIZAR O SAQUE'''
# 1
if banco.autenticar(cliente1):
    cliente1.conta.depositar(100)
    cliente1.conta.sacar(20)
else:
    print("Cliente não autenticado")
print('##################################')
# 2
if banco.autenticar(cliente3):
    cliente3.conta.depositar(0)
    cliente3.conta.sacar(20)
else:
    print("Cliente não autenticado")
