from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    codigo: int         = 0
    senha_atual: str    = ''
    fila                = []
    clientes_atendidos  = []

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, Caixa: {caixa}'

    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {'dia': dia, 'agencia': agencia,
                           'clientes atendidos': self.clientes_atendidos,
                           'quantidade de clientes atendidos':
                               len(self.clientes_atendidos)}
        return estatistica
