from collections import Counter

texto = "Bem vindo meu nome é Elias irei falar sobre os meus gostos " \
        "eu gosto muito de cachorros e gatos eu gosto também de beber café"
texto = texto.lower()

aparicoes = Counter(texto.split())

print(aparicoes)