from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
         transacao.registrar(conta)

    def adicionar_conta(self, conta):
         self.conta.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
         super().__init__(endereco)
         self.nome = nome
         self.data_nascimento = data_nascimento
         self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
       return cls(numero, cliente)

    @property
    def saldo (self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def agencia(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente para saque.")
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Falha na operacao!")
        
        return False    

    def depositar(self, valor):

        if ( valor > 0 ):
            self._saldo += valor
            print("Deposito realizado!")
        
        else:
            print("Valor invalido, tente novamente!")
            return False

        return True

class ContaCorrete(Conta):

    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__nome__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Excedeu limite de saque!")

        elif excedeu_saques:
            print("Numero maximo de saques realziados!")

        else:
            return super().sacar(valor)    

        return False

    def __str__(self):
        return f"""\
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titulo:\t{self.cliente.nome}
        """ 

class Historico:
    def __init__(self):
        selft = _transacoes = []

    @property
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self._transacao.append(
            {
                "tipo":transacao.__class__.__nome__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():

            menu = """ 
                        BANCO PYX 3.0
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Cadastrar Usuario
            [5] Cadastrar Conta
            [6] Listar Contas
            [0] Sair

            =>"""
            return int(input(menu))

def cadastrar_usuario(usuarios):
    
     cpf = input("Digite o CPF: ")
     usuario = filtrar_usuario(cpf,usuarios)

     if usuario:
        print("Usuario possui cadastro")

        return
     nome = input("Digite o nome: ")
     dt_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Infome o endereco (logradouro, numero, bairro - cidade/sigla do estado): ")
     usuarios.append({"nome:":nome, "dt_nascimento":dt_nascimento, "cpf": cpf, "endereco": endereco})

     print("Usuario cadastrado!")

def filtrar_cliente(cpf, clientes):
   clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf ]
   return clientes_filtrados[0] if clientes_filtrados else None  

def cadastrar_conta(agencia, numero_conta, usuarios):

    cpf = input("Digite o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("Conta criada com sucesso!")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario nao cadastrado!")

def listar_contas (contas):
    
    if contas == []:
        print("Nenhuma conta cadastrada!")
    else:   
        for conta in contas:
            linha = f"""
    Agencia: {conta['agencia']}
    Conta Corrente: {conta['numero_conta']}
    Titular: {conta['usuario']}
    """
            print("=" * 80)
            print(linha)
            print("=" * 80)

def recuperar_conta_cliente(cliente):
    pass

def depositar(clientes):
    cpf = input("informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("Cliente nao cadastrado!")
        return
    
    valor = float(input("Informe o valor do deposito:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def main():

    clientes = []
    contas = []

    while True:
    
        opcao = menu()

        if opcao == 1: # Opcao de deposito

            depositar(clientes)

        elif opcao == 2: # Opcao de saque

            sacar(clientes)

        elif opcao == 3: # Opção de extrato

            exibir_extrato(clientes)

        elif opcao == 4: # Opção de cadastrar usuario
             
           criar_cliente(clientes) 
        
        elif opcao == 5: # Opção de cadastrar conta

           numero_conta = len(contas)+1
           criar_conta(numero_conta, clientes, contas)  
        
        elif opcao == 6: # Opção de listar conta
             
            listar_contas(contas)

        elif opcao == 0: # Opção de sair da aplicação
            print('''
            Obrigado por utilizar nosso servico!
            ''')
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
