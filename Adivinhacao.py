
import random

print('***************************************')
print('**********Jogo da adivinhação**********')
print('***************************************')

numero_secreto = random.randint(1, 100)
total_tentativas = 5

print("Qual a dificuldade?")
print("1(15 chances), 2(10 chances), 3(5 chances)")

dificuldade = int(input("Defina o nível: "))

if (dificuldade == 1):
    total_tentativas = 15

if (dificuldade == 2):
    total_tentativas = 10

elif (dificuldade == 3):
    total_tentativas = 5

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    
    chute_str = input("Digite o seu número de 1 a 100:")

    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue

    print("Seu número é: ", chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("Você acertou!!")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")

print(numero_secreto)
print("Fim de jogo")