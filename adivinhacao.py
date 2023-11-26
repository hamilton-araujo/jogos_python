import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = int(100*random.random())

chute = input("Digite o número que você deseja chutar. ")

if numero_secreto == chute:
    print("Você acertou.")
else:
    print("Você errou. Tente Novamente")