import random
import os

jogo = True

while jogo == True:

    os.system('cls')

    print('Bem vindo ao Número Secreto O JOGO!\nversão 1.2.2')
    

    

    def modo_doJogo():
        while True:

            print('\nPor Favor, escolha uma dificuldade:\n[f = Fácil.]\n[m =  Médio.]\n[d = Difícil.]')
            escolha = (input('Digite aqui:  ')).lower()
            
            match escolha:

                case "f":
                    print(f'\nVocê escolheu o nível de dificuldade Fácil.\nVocê tem o total de  7 vidas.\nO número de 1 à 10 ')
                    return 6, random.randint (0,11)
        
                case 'm':
                    print(f'\nVocê escolheu o nível de dificuldade Médio.\nVocê tem o total de  8 vidas.\nO número de 1 à 25 ')
                    return 8, random.randint (0,26)
        
                case 'd':
                    print(f'\nVocê escolheu o nível de dificuldade Difícil.\nVocê tem o total de 10 vidas.\nO número vai de 1 à 50')
                    return 10, random.randint (0,50)

                case _:
                    print(f'\nEscolha "{escolha}" inválida.\n Por favor escolha entre f, m ou d')

    vidas, numeromagico = modo_doJogo()

    vitoria = False    
    while vitoria == False and vidas > 0:
        try:
            chute = int(input("\nAdivinhe qual é o número que estou pensando..."))
        except ValueError:
            print (f'\nOpção {chute} inválida. Digite um número.')
        
        
        if chute == numeromagico:
            print("\nParabéns, você acertou!")
            vitoria = True
        else:
            while vidas != 0:
                vidas -= 1
                print(f"Você errou. Ainda tem {vidas} vidas restantes.")
                if chute < numeromagico:
                    print ("\nTente maior!")
                else:
                    print ("\nTente menor!")
            if not vidas:
                print("\nVocê errou e não tem mais vidas restantes...")
        
    if vitoria == True or not vidas:

        print('\nO jogo acabou...')        
        print('Deseja Jogar novamente?')
        print('[ s = Sim ]')
        print('[ n = Não ]')

        denovo = (input(':__')).lower()
        if denovo == 's':
            print('\nCerto, Reiniciando o jogo...')
            print('\nBoa sorte!')
            vitoria = False

        if denovo == 'n':
            print('\nObrigado por jogar, até a próxima!')
            jogo = False

        else:
            print(f'\nOpção {denovo} inválida. Por favor escolha entre "s" ou "n"')
