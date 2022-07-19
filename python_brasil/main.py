from cpf_cnpj import Documento
from telefone import TelefonesBR

cpf     = 86075244026
cnpj    = 58980620000114
numero  = 1281120537045
documento  = Documento.criar_documento(cpf)
documento2 = Documento.criar_documento(cnpj)
telefone   = TelefonesBR(numero)

print(documento)
print(documento2)
print(telefone)
