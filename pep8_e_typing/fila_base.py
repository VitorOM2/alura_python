import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo = 0
    senha_atual = None
    fila = []
    clientes_atendidos = []

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> None:
        ...

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    def inseri_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
