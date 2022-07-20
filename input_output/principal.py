arquivo = open('/home/vmarques/Alura_Python/input_output/dados/contatos.csv',
                encoding='latin_1')

for linha in arquivo:
    print(linha, end='')