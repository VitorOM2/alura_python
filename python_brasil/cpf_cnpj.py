from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def criar_documento(documento):

        doc_str = str(documento)

        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        else:
            raise ValueError("Documento inválido!!")


class DocCpf:

    def __init__(self, documento):
        if self.validar(documento):  # Chama a função de verificar
            self.documento = documento    # Se o CPF for válido atribui o valor
        else:
            raise ValueError("CPF inválido!")  # Chama um erro se o CPF for inválido

    def __str__(self):
        return f"CPF: {self.format()}"  # Chama a função para criar a máscara

    def validar(self, documento):  # Verificador
        validador = CPF()
        return validador.validate(documento)

    def format(self):  # Define o formato da máscara
        mascara = CPF()
        return mascara.mask(self.documento)


class DocCnpj:

    def __init__(self, documento):
        if self.validar(documento):
            self.documento = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return f"CNPJ: {self.format()}"

    def validar(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)
