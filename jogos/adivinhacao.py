import random


def jogar():
    print('=================================')
    print('Bem vindo ao jogo de Adivinhação!')
    print('=================================')

    numero_secreto   = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000
    dificuldade = int(input('Escolha a dificuldade (1)Fácil (2)Médio (3)Difícil: '))

    if dificuldade       == 1:
        total_tentativas = 10
    elif dificuldade     == 2:
        total_tentativas = 8
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):

        print('\nTentativa {} de {}'.format(rodada, total_tentativas))
        chute = int(input('\nDigite um número de 1 a 100: '))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número de 1 a 100")
            continue

        print('\nSeu número é: ', chute)

        if chute == numero_secreto:
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if chute > numero_secreto:
                print('Você errou! O seu chute foi maior do que o número secreto')
            elif rodada == total_tentativas:
                print("O número secreto era {} e você fez {} pontos".format(numero_secreto, pontos))
            else:
                print('Você errou! O seu chute foi menor do que o número secreto')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print('\nFim de Jogo!')
