from testes.bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self) -> None:
        entrada: str = '13/03/2000'  # Given - Contexto
        esperado: int = 22
        funcionario_teste: object = Funcionario('Teste', entrada, 1111)  # When - Ação
        resultado: int = funcionario_teste.idade()

        assert resultado == esperado  # Then - Desfecho

