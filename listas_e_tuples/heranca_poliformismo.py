import array as arr
from abc import ABCMeta, abstractmethod


class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __str__(self):
        return f"\n>> Código: {self._codigo}\n>> Saldo: {self._saldo}"

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self._codigo == other._codigo

    @abstractmethod
    def passa_o_mes(self):
        raise NotImplemented
        pass

    def deposita(self, valor):
        self._saldo += valor


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


array = arr.array('d', [1, 3.5])

conta2      = ContaCorrente(2)
conta3      = ContaPoupanca(3)
conta4      = ContaPoupanca(4)
contas      = (conta2, conta3)
usuarios    = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]
idades = (18, 25, 29, 36)


conta2.deposita(500)
conta3.deposita(500)

print(conta2)
print(conta3)

for conta in contas:
    conta.passa_o_mes()  # Duck typing

print(conta2)
print(conta3)

print(conta2 == conta3)

for nome, idade, nascimento in usuarios:
    print(f"\n>> Nome: {nome}")

for indice, idade in enumerate(idades):
    print(f"\n>> Indice: {indice} >> Idade: {idade}")

