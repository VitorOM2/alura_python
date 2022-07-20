try:
    with open('dados/contatos.csv', encoding='latin_1') as arquivo:
        for linha in arquivo:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permisão de escrita')
