class Programa():
    def __init__(self,nome, ano):
        self._nome = nome
        self.ano   = ano
        self._like = 0

    # =============== GETTERS ===============
    @property
    def like(self):
        return self._like

    @property
    def nome(self):
        return self._nome

    # =============== SETTERS ===============
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # =============== MÉTODOS: Variados ===============
    def dar_likes(self):
        self._like += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} - {vingadores.like}')

himym = Serie('how i met your mother', 2005, 9)
print(f'\nSérie: {himym.nome} \nAno de lançamento: {himym.ano} \nTemporadas: {himym.temporadas} - {himym.like}')
