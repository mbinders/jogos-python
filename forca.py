def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')
    print('\n')

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):

        chute = input("Informe uma letra? ")
        chute = chute.strip()
        index = 1

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra '{}' na posicao '{}'".format(letra, index))

            index += 1

        print("jogando")

    print('Game Over')

if (__name__ == '__main__'):
    jogar()