class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print('A data formatada é: {:02d}/{:02d}/{}'.format(self.dia, self.mes, self.ano))


data = Data(26, 6, 2022)
data.formatada()

