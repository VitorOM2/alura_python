def jogar():
    print('=================================')
    print('   Bem vindo ao jogo da forca!   ')
    print('=================================')

    palavra_secreta = "banana"
    enforcou = False
    ganhou   = False

    while not enforcou and not ganhou:
        chute = input("Qual letra? ").strip()
        index = 0

        for letra in palavra_secreta:  # Loop para iterar a string
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {} ".format(chute, index))
            index = index + 1  # Acrescenta uma posição no index para cada letra
        print("Jogando...")


if __name__ == "__main__":
    jogar()
