import random


def jogar():
    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()
    letras_certas = inciar_letras_certas(palavra_secreta)
    print(letras_certas)

    enforcou = False
    ganhou = False
    erros = 0

    while not enforcou and not ganhou:
        chute = pede_chute()

        if chute not in palavra_secreta:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)
        else:
            marca_chute_correto(chute, letras_certas, palavra_secreta)

        enforcou = erros == 7
        ganhou = "_" not in letras_certas
        print(letras_certas)

    if ganhou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


def imprime_mensagem_inicial():
    print('=================================')
    print('   Bem vindo ao jogo da forca!   ')
    print('=================================')


def carrega_palavra_secreta():

    arquivo = open("palavras.txt", 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inciar_letras_certas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute


def marca_chute_correto(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:  # Loop para iterar a string
        if chute == letra:
            letras_certas[index] = letra
        index += 1  # Acrescenta uma posição no index para cada letra


def mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \        ")
        print("  /                 \       ")
        print("//                   \/\    ")
        print("\|   XXXX     XXXX   | /    ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/      ")
        print("   |\     XXX     /|        ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/        ")
        print("     \_         _/          ")
        print("       \_______/            ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
