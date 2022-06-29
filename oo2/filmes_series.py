class Programa():
    def __init__(self, nome, ano):
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

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self._like}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'\nNome: {self._nome} \nAno: {self.ano}' \
               f'\nDuração: {self.duracao} min  \nLikes: {self._like}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'\nNome: {self._nome} \nAno: {self.ano}' \
               f'\nDuração: {self.temporadas} temporadas  \nLikes: {self._like}'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
himym = Serie('how i met your mother', 2005, 9)
himym.dar_likes()
himym.dar_likes()

lista = [vingadores, himym]

for programa in lista:
    print(programa)
