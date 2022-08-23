from datetime import date


class Funcionario:
    def __init__(self, nome: str, data_nascimento: str, salario: float):
        self._nome: str = nome
        self._data_nascimento: str = data_nascimento
        self._salario: float = salario

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def salario(self) -> str:
        return self._salario

    def idade(self) -> int:
        data_nasciemnto_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nasciemnto_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self) -> float:
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self) -> str:
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'