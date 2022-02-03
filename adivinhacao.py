#importando aleatoriedade
import random
#definição do código
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
#definindo o numero para acertar, total de tentativas do jogo e quantos pontos se inicia // range: define uma serie de valores
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
#mensagem para escolher a dificuldade
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
#digitando o nivel escolhido
    nivel = int(input("Defina o nível: "))
#quantas tentativas para qual nivel escolher
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
#mostrando quantas tentativas restam
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#mostrando o numero que você digitou
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
#capando a possibilidade de escrever um numero menor que 1 e maior que 100
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
#difinindo variaveis de acerto, numero menor e numero maior
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
#caso acerte o numero ou digite um numero maior ou menor informa a condição e total de pontos feitos
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
#demonstra fim de jogo
    print("Fim do jogo")
#formatando para escolha em outro projeto


if (__name__ == "__main__"):
    jogar()