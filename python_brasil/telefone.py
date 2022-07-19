import re

class TelefonesBR:

    def __init__(self, telefone):

        telefone = str(telefone)

        if self.validar(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Número incorreto")

    def __str__(self):
        return f"Número: {self.format()}"

    def validar(self, telefone):
        padrao   = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format(self):
        padrao  = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resp    = re.search(padrao, self.telefone)
        mascara = f"+{resp.group(1)}({resp.group(2)}){resp.group(3)}-{resp.group(4)}"
        return mascara
