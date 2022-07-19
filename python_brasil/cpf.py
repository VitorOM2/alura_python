class Cpf:

    def __init__(self, documento):
        documento = str(documento)

        if self.verifica_cpf(documento):  # Chama a função de verificar
            self.documento = documento    # Se o CPF for válido atribui o valor
            print("ok")
        else:
            raise ValueError("CPF inválido!")  # Chama um erro se o CPF for inválido

    def verifica_cpf(self, documento):  # Verificador
        if len(documento) == 11:        # Verifica o tamanho do CPF
            return True
        else:
            return False
