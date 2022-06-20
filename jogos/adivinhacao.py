print('=================================')
print('Bem vindo ao jogo de Adivinhação!')
print('=================================')

numero_secreto = 8
chute          = int(input('Digite o seu número: '))

if chute == numero_secreto:
    print('Você acertou!')
else:
    if chute > numero_secreto:
        print('Você errou! O seu chute foi maior do que o número secreto')
    else:
        print('Você errou! O seu chute foi menor do que o número secreto')
