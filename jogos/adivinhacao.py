import random

print('=================================')
print('Bem vindo ao jogo de Adivinhação!')
print('=================================')

numero_secreto = random.randrange(1, 101)
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):

    print('\nTentativa {} de {}'.format(rodada, total_tentativas))
    chute = int(input('\nDigite um número de 1 a 100: '))

    if chute < 1 or chute > 100:
        print("Você deve digitar um número de 1 a 100")
        continue

    print('Seu número é: ', chute)

    if chute == numero_secreto:
        print('Você acertou!')
        break
    else:
        if chute > numero_secreto:
            print('Você errou! O seu chute foi maior do que o número secreto')
        else:
            print('Você errou! O seu chute foi menor do que o número secreto')

print('\nFim de Jogo!')
