class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo  = 0

    def __str__(self):
        return f"\n>> Código: {self._codigo}\n>> Saldo: {self._saldo}"

    def deposita(self, valor):
        self._saldo += valor


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


conta2 = ContaCorrente(2)
conta3 = ContaPoupanca(3)

conta2.deposita(500)
conta3.deposita(500)

print(conta2)
print(conta3)
