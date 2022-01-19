import random

def jogar():
    print('*********************************')
    print('Que os jogos comecem...', 'certo!?')
    print('*********************************')
    print('\n')

    numero_secreto = 0
    tentativa = 1
    total_de_tentativas = 0
    limite_max_numero = 0
    pontos = 1000

    print('Por favor, selecione o nivel desejado')
    nivel = int(input('(1) Facil (2) Medio (3) Dificil: '))

    if (nivel == 1):
        total_de_tentativas = 20
        limite_max_numero = 50
    elif (nivel == 2):
        total_de_tentativas = 10
        limite_max_numero = 70
    else:
        total_de_tentativas = 5
        limite_max_numero = 100

    numero_secreto = round(random.randrange(1, limite_max_numero + 1))

    print('Por favor, informar um numero entre 1 e {}\n'.format(limite_max_numero))


    ### USO DO WHILE ###

    while (tentativa <= total_de_tentativas):
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute = int(input("Digite um numero: "))

        print("Vc digitou", chute)

        if (chute < 1 or chute > limite_max_numero):
            print('Vc digitou um numero fora do limite aceitavel, tente de novo..\n')
            tentativa += 1
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if (acertou):
            print("Parabens! Vc acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if (maior):
                print("Vc errou para cima")
            elif (menor):
                print("Vc errou para baixo")

            if (tentativa != total_de_tentativas):
                print("Vms tentar novamente?\n")
            elif (tentativa == total_de_tentativas):
                print("Que pena, vc não acertou o numero secreto {} \n".format(numero_secreto))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        tentativa += 1

    ### USO DO FOR ###
    print("Agora vms tentar de novo em outro modo...")

    for tentativa_for in range(1, total_de_tentativas + 1):
        print("Tentativa For {} de {}".format(tentativa_for, total_de_tentativas))
        chute = int(input("Digite um numero: "))
        print("Vc digitou", chute)

        if (chute < 1 or chute > limite_max_numero):
            print('Vc digitou um numero fora do limite aceitavel, tente de novo..\n')
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if (acertou):
            print("Parabens! Vc acertou!\n")
            break
        else:
            if (maior):
                print("Vc errou para cima")
            elif (menor):
                print("Vc errou para baixo")

            if (tentativa_for != total_de_tentativas):
                print("Vms tentar novamente?\n")
            elif (tentativa_for == total_de_tentativas):
                print("Que pena, vc não acertou o numero secreto {} \n".format(numero_secreto))

    print("Game over")

if (__name__ == '__main__'):
    jogar()