import adivinhacao
import forca

def jogar():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca\n")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        forca.jogar()

jogar()