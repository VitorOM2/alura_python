def jogar():
    print('=================================')
    print('   Bem vindo ao jogo da forca!   ')
    print('=================================')

    palavra_secreta = "banana"
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    ganhou   = False

    print(letras_certas)

    while not enforcou and not ganhou:
        chute = input("Qual letra? ").strip()
        index = 0

        for letra in palavra_secreta:  # Loop para iterar a string
            if chute.upper() == letra.upper():
                letras_certas[index] = letra
            index = index + 1  # Acrescenta uma posição no index para cada letra

        print(letras_certas)


if __name__ == "__main__":
    jogar()
