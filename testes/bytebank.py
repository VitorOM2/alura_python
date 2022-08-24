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
        data_nascimento_quebrada: list = self._data_nascimento.split('/')
        ano_nascimento: str = data_nascimento_quebrada[-1]
        ano_atual: int = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self) -> str:
        nome_completo: str = self.nome.strip()
        nome_quebrado: str = nome_completo.split(' ')
        return  nome_quebrado[-1]

    def _eh_socio(self) -> bool:
        sobrenomes: list = ['Bragança', 'Windsor', 'Bourbon', 'Yamato',
                            'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']

        return self._salario >= 100000 and self.sobrenome() in sobrenomes

    def decrescimo_salario(self) -> None:
        if self._eh_socio():
            decrescimo = self._salario - (self.salario * 0.1)
            self._salario = decrescimo

    def calcular_bonus(self) -> float:
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self) -> str:
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
