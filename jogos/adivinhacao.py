print('=================================')
print('Bem vindo ao jogo de Adivinhação!')
print('=================================')

numero_secreto = 8
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):

    print('\nTentativa {} de {}'.format(rodada, total_tentativas))
    chute = int(input('\nDigite o seu número: '))
    print('Seu número é: ', chute)

    if chute == numero_secreto:
        print('Você acertou!')
    else:
        if chute > numero_secreto:
            print('Você errou! O seu chute foi maior do que o número secreto')
        else:
            print('Você errou! O seu chute foi menor do que o número secreto')

print('\nFim de Jogo!')
