from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        documento = str(documento)

        if self.verifica_cpf(documento):  # Chama a função de verificar
            self.documento = documento    # Se o CPF for válido atribui o valor
        else:
            raise ValueError("CPF inválido!")  # Chama um erro se o CPF for inválido

    def __str__(self):
        return f" CPF: {self.format_cpf()}"  # Chama a função para criar a máscara

    def verifica_cpf(self, documento):  # Verificador
        if len(documento) == 11:        # Verifica o tamanho do CPF
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválidos")

    def format_cpf(self):  # Define o formato da máscara
        mascara = CPF()
        return mascara.mask(self.documento)
