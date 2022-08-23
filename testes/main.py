from testes.bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2001', 1111)
    print(f'Teste = {funcionario_teste.idade()} ')

    funcionario_teste1 = Funcionario('Teste1', '10/03/2001', 1100)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste2', '14/03/2000', 1000)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()
