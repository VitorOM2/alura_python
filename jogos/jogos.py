import adivinhacao
import forca

print("====================")
print("   Escolha o jogo   ")
print("====================")

jogo = int(input("\n(1) Adivinhação (2) Forca"))

if jogo == 1:
    adivinhacao.jogar()
elif jogo == 2:
    forca.jogar()

