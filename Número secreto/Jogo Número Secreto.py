import random
import os

jogo = True
while jogo == True:

    os.system('cls')

    print('\nBem vindo ao Número Secreto O JOGO!\nversão 1.2.2')

    dificuldade = True

    while dificuldade == True:

        print('Por Favor, escolha uma dificuldade:\n[f = Fácil.]\n[m =  Médio.]\n[d = Difícil.]')

        escolher_dificuldade = (input('Digite aqui:__'))

    def modo_doJogo(escolher_dificuldade):
        global numeromagico
        global vidas

        match escolher_dificuldade:
                case "f":
                    vidas = 6
                    numeromagico = random.randint (0,11)
                    print(f'Você escolheu o nível de dificuldade Fácil.\nVocê tem o total de  7 vidas.\nO número de 1 à 10 ')
                    break
        
                case 'm':
                    vidas = 8
                    numeromagico = random.randint (0,26)
                    print(f'Você escolheu o nível de dificuldade Médio.\nVocê tem o total de  8 vidas.\nO número de 1 à 25 ')
                    break
        
                case 'd':
                    nivel = 'Difícil'
                    vidas = 10
                    numeromagico = random.randint (0,51)
                    print(f'Você escolheu o nível de dificuldade Difícil.\nVocê tem o total de 10 vidas.\nO número vai de 1 à 50')
                    break

                case _:
                    print(f'Escolha "{escolher_dificuldade}" inválida.\n Por favor escolha entre f, m ou d')    
            
    vitoria = False
    while vitoria == False and vidas > 0:
        chute = int(input("Adivinhe qual é o número que estou pensando..."))
        
        if chute == numeromagico:
            print("boa")
            vitoria = True
        else:
            vidas -= 1
            print(f"Você errou. ainda tem {vidas} vidas restantes.")
            if chute < numeromagico:
                print ("Tente maior")
            else:
                print ("Tente menor")
                
    if vidas == 0:
        print("Você não tem mais vidas restantes.")
        
    if vitoria == True or vidas == 0:
        print('O jogo acabou...')        
        print('')
        print('Deseja Jogar novamente?')
        print('')
        print('[ s = Sim ]')
        print('[ n = Não ]')
        denovo = (input(':__'))
        if denovo == 's':
            print('')
            print('Certo, Reiniciando o jogo...')
            print('Boa sorte!')
            vitoria = False   
        if denovo == 'n':
            print('Obrigado por jogar, até a próxima!')
            jogo = False
        else:
            print(f'Opção {denovo} inválida. Por favor escolha entre "s" ou "n"')
        