import contatos_utils

try:
    contatos = contatos_utils.csv_para_contatos
    ('/home/vmarques/Alura_Python/io/dados/contatos.csv')
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
    
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permisão de escrita')