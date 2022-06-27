class Conta:

    def __int__(self, numero, titular, saldo, limite):
        self.numero  = numero
        self.titular = titular
        self.saldo   = saldo
        self.limite  = limite

    def extrato(self):
        print("Extrato: {}".format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
