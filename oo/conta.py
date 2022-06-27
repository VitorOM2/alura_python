class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite

    def extrato(self):
        print("Extrato: {}".format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __poder_sacar(self, valor):
        valor_disponivel = self.saldo + self.limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if self.__poder_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # =============== Getters ===============
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # =============== Setters ===============
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # =============== Estáticos ==============
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}