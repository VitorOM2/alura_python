from cpf_cnpj import Documento

cpf  = 86075244026
cnpj = 58980620000114
documento  = Documento.criar_documento(cpf)
documento2 = Documento.criar_documento(cnpj)

print(documento)
print(documento2)
