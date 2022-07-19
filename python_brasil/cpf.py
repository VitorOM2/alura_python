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
            return True
        else:
            return False

    def format_cpf(self):  # Define o formato da máscara
        fatia1 = self.documento[:3]
        fatia2 = self.documento[3:6]
        fatia3 = self.documento[6:9]
        fatia4 = self.documento[9:]
        return f"{fatia1}.{fatia2}.{fatia3}-{fatia4}"
