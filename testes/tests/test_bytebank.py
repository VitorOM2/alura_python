from testes.bytebank import Funcionario

import pytest

from pytest import mark


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self) -> None:
        entrada: str = '13/03/2000'  # Given - Contexto
        esperado: int = 22
        funcionario_teste: object = Funcionario('Teste', entrada, 1111)  # When - Ação
        resultado: int = funcionario_teste.idade()

        assert resultado == esperado  # Then - Desfecho

    def test_quando_sobrenome_recebe_charles_xavier_deve_retornar_xavier(self) -> None:

        entrada: str = 'Charles Xavier'  # Given - Contexto
        esperado: str = 'Xavier'
        charles_xavier: object = Funcionario(entrada, '10/03/1932', 10000)  # When - Ação
        resultado: int = charles_xavier.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self) -> None:
        entrada_salario: float = 100000
        entrada_nome: str = 'Paulo Bragança'
        esperado: float = 90000

        funcionario_teste: object = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()

        resultado: float = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self) -> None:
        entrada: float = 1000
        esperado: float = 100

        funcionario_teste = Funcionario('teste', '01/01/2001', entrada)

        resultado: float = funcionario_teste.calcular_bonus()
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self) -> None:
        with pytest.raises(Exception):
            entrada = 100000

            funcionario_teste = Funcionario('teste', '01/01/2001', entrada)

            resultado = funcionario_teste.calcular_bonus()
            assert resultado
