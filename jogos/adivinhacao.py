print('=================================')
print('Bem vindo ao jogo de Adivinhação!')
print('=================================')

numero_secreto = 8
chute = int(input('Digite o seu número: '))

if numero_secreto == chute:
    print('Você acertou!')
else:
    print('Você errou!')
