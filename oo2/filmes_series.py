class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    # =============== GETTERS ===============
    @property
    def like(self):
        return self.__like

    @property
    def nome(self):
        return self.__nome

    # =============== SETTERS ===============
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # =============== MÉTODOS: Variados ===============
    def dar_likes(self):
        self.__like += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__like = 0

    # =============== GETTERS ===============
    @property
    def like(self):
        return self.__like

    @property
    def nome(self):
        return self.__nome

    # =============== SETTERS ===============
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def dar_likes(self):
        self.__like += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'{vingadores.nome}')

himym = Serie('how i met your mother', 2005, 9)
print(f'\nSérie: {himym.nome} \nAno de lançamento: {himym.ano} \nTemporadas: {himym.temporadas}')
