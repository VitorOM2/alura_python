print('=================================')
print('Bem vindo ao jogo de Adivinhação!')
print('=================================')

numero_secreto = 8
rodada = 1
total_tentativas = 3

while rodada <= total_tentativas:

    chute = int(input('Digite o seu número: '))
    print('Tentativa:', rodada, 'de', total_tentativas)
    print('Seu número é: ', chute)

    if chute == numero_secreto:
        print('Você acertou!')
    else:
        if chute > numero_secreto:
            print('Você errou! O seu chute foi maior do que o número secreto')
        else:
            print('Você errou! O seu chute foi menor do que o número secreto')

    rodada = rodada + 1

print('Fim de Jogo!')
