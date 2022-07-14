class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo  = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"\n>> Código: {self._codigo}\n>> Saldo: {self._saldo}"


conta_teste = Conta(1)
conta_teste.deposita(500)
print(conta_teste)
