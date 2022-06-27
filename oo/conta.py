class Conta:

    def __int__(self, numero, titular, saldo, limite):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite

    def extrato(self):
        print("Extrato: {}".format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
