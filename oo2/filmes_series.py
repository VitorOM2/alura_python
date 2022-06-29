class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano  = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano  = ano
        self.temporadas = temporadas
        self.__likes = 0


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(vingadores.nome)
