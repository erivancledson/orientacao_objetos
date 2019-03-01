class Conta:

    'construtor'
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        '__ antes do nome da variavel significa private'
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    'o metodo nao fica visivel é privado'
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))



    'conta2.transfere(10.0, conta)'
    def transfere(self, valor,  destino):
        self.saca(valor)
        destino.deposita(valor)

    'getters'

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    'nesse get usa busca assim, conta.limite'
    @property
    def limite(self):
        return self.__limite
    'set conta.limite = 2000'
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    'metodo estatico'
    'é da classe acessa Conta.codigo_banco'
    @staticmethod
    def codigo_banco(self):
        return "001"


    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}