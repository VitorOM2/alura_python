arquivo = open('dados/contatos.csv',
               encoding='latin_1')

for linha in arquivo:
    print(linha, end='')
