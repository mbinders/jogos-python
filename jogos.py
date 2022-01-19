import forca
import adivinhacao

def escolhe_jogo():
    print('*********************************')
    print('*******Escolha o seu jogo!*******')
    print('*********************************')
    print('\n')

    jogo = int(input('(1) Forca  (2) Adivinhação (9) Sair: '))

    if (jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando Adivinhacao')
        adivinhacao.jogar()
    elif (jogo == 9):
        print('Obrigado, ate a próxima!')
    else:
        print('Opcao invalida, selecionei uma opção válida!')

if (__name__ == '__main__'):
    escolhe_jogo()