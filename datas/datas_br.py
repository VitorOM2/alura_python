from datetime import datetime, timedelta


class Cadastro:

    def __init__(self):
        self.data_cadastro = datetime.today()
        self.tempo_cadastro()

    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=8, minutes=8, seconds=8)
        return agora - self.data_cadastro
