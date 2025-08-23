import random

nome = str(input("Olá, Aventureiro! Qual seu nome?: "))

classes = {
    '1': "Guerreiro",
    '2': "Mago",
    '3': "Arqueiro"
}

print("Conheça as classes de honra:")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")
print("Qualquer outro dígito - Aventureiro")

classe_opcao = str(input(f"Olá, {nome}, escolha qual será sua classe: "))

classe_opcao = classes.get(classe_opcao, "Aventureiro")

print(f"Grande {nome}, o {classe_opcao}!")
print("\n")

print("Nas terras esquecidas de Eldoria, conta-se sobre um colar que guarda poder oculto protegido nas ruínas de um antigo castelo.")
print("Dizem que apenas os mais corajosos conseguem atravessar as armadilhas, monstros e enigmas que protegem o artefato sagrado.")
print(f"Agora, o destino recai sobre você, {nome}, o valente {classe_opcao}, que parte em busca dessa relíquia lendária.")

hp = 10

game_over = False

while hp > 0 and not game_over:

    print("\n")
    print("Depois de andar por 4 dias com o auxílio de uma mapa mágico, você chega às ruínas de Eldoria. Diante de você, duas entradas:")
    print("1 - O PORTÃO PRINCIPAL, parcialmente destruído e enferrujado, levemente iluminado pela lua.")
    print("2 - UM TÚNEL LATERAL, escuro e estreito, de onde ecoam estranhos sons.")
    print("3 - FUGIR.")

    escolha = int(input("Você percebe que precisa escolher entre elas duas, e sua decisão é: "))

    if escolha == 1:

        print("\nVocê decide entrar pelo portão principal.")
        print("Você encontra em frente dois esqueletos GIGANTES com espadas que bloqueiam sua passagem.")
        print("1 - ATACAR")
        print("2 - DEFENDER")
        print("3 - FUGIR")

        acao = int(input(f"O que você, {nome}, decide fazer?: "))

        if acao == 1:

            print("Arduamente você consegue derrota-los e entrar no reino.")
            print("Mas os contra-ataques foram dolorosos, fazendo-o perder -3 de HP.")
            hp -= 3
            print(f"HP: {hp}\n")

        elif acao == 2:

            print("Você consegue se defender muito bem, mas durante a luta, houve momentos em que não teve como se desviar de certos golpes, fazendo-o perder -1 de HP.")
            hp -= 1
            print(f"HP: {hp}\n")

        else:

            print("Você percebe o quão grande são os esqueletos e quão afiada são suas espadas.")
            print("Dessa forma, você decide fugir e aborta a missão.")
            print("GAME OVER")
            game_over = True

    elif escolha == 2:

        print("\nVocê decide entrar pelo túnel.")
        print("Ao chão, você encontra um pergaminho brilhando em dourado e é tomado por uma curiosidade imensa.")
        print("Você pega esse pergaminho, abre e...")

        valor_pergaminho = int(input("Digite um número de 1 a 10: "))

        if valor_pergaminho % 2 == 0:

            print("O pergaminho brilha em verde e ele te dá +3 de HP!")
            hp += 3
            print(f"HP: {hp}")
        else:

            print("O pergaminho brilha em vermelho e explode na sua mão, e assim você perde -2 de HP")
            hp -= 2
            print(f"HP: {hp}")

    else:

        print("Você decide fugir e desiste da missão...")
        print("GAME OVER")
        game_over = True

    if hp <= 0 or game_over:
        break

    input("\nPressione ENTER para continuar...")
    print("Ao entrar no reino de Eldoria, você encontra um armazém antigo e decide entrar.")
    print("Dentro dele, há um espelho em uma parede. Você percebe que de alguma forma ele está sussurrando: 'Escolha sua verdade, e o caminho será revelado.'")
    print("\n1 - Você olha seu reflexo pelo espelho.")
    print("2 - Você ignora o espelho e foca na missão.")

    escolha = int(input(f"O que você, {nome}, decide fazer?: "))
    print("\n")

    if escolha == 1:

        print("Ao se olhar pelo reflexo, percebe que aquilo era uma armadilha mágica e fica totalmente atordoado.")
        print("O espelho diz para você adivinhar um número entre 1 a 6, caso erre, perderá um número aleatório de HP.")
        print("Você tem 3 tentativas.\n")

        num_secreto = random.randint(1, 6)

        tentativas = 3

        adivinha_num = 0

        while adivinha_num != num_secreto and tentativas > 0:

            adivinha_num = int(input("Adivinhe o número entre 1 a 6: "))

            tentativas -= 1

            if adivinha_num == num_secreto:

                print("Parabéns! Você acertou o número!")
                print("Você consegue escapar e sai intacto!!")
            else:

                if tentativas > 0:

                    print(f"Errado! Nova chance. Você ainda tem {tentativas} tentativas.")

                else:
                    dano = random.randint(1, 3)
                    print("Você errou!")
                    print(f"O número era {num_secreto}.")
                    print(f"Você perdeu {dano} de HP.")
                    hp -= dano
                    print(f"HP: {hp}")

    elif escolha == 2:

        print("Como você é bem treinado, conhece técnicas malígnas e imagina que possa ser uma armadilha e decide ignorar o espelho e continuar a missão.")
        print("+1 de HP por autoconfiança.")
        hp += 1
        print(f"HP: {hp}")

    else:

        print("Você sente um medo muito grande e decide fugir...")
        print("GAME OVER")
        game_over = True

    if hp <= 0 or game_over:
        break

    print("\nDepois de sair do armazém, você finalmente chega no castelo e encontra um baú de madeira em um santuário com estátuas ao seu redor.")
    print("1 - Você decide abrir")
    print("2 - Você ignora o baú")

    escolha = int(input(f"O que você, {nome}, decide fazer?: "))
    print("\n")

    if escolha == 1:

        resposta_charada = "Nome"

        print("Ao abrir o baú, surge um rosto feito de fumaça e ele te diz: ")
        print("'Ao abrir o baú, a charada deve acertar!'")
        print("'O que pertence a você, mas os outros usam mais do que você?'")

        resposta_usuario = input("O que é?: ")

        
        if resposta_charada.casefold() == resposta_usuario.casefold(): # .casefold() se assemelha ao .equalsIgnoreCase do java
            print("CERTA RESPOSTA!!\n")
            print("A fumaça começa a ficar maior e se transforma em um monstro gigante usando um colar com um pingente em formato de sol.")
            print("Ao ver o colar no pescoço do monstro, você percebe que aquele é o artefato que armazena o poder que você estava à procura.")
            print("1 - Lutar")
            print("2 - Fugir")

            escolha = int(input(f"O que você, {nome}, decide fazer?: "))

            if escolha == 1:

                hp_monstro = 10

                print("\nOs seus ataques e do inimigo serão feitos através de sorte.")
                print("Será gerado um número, se for PAR o ataque é concluído.")
                print("Se for ÍMPAR, o ataque falha.")
                print(f"Os danos de ambos ({nome} e Monstro) são aleatórios de 1 a 6.")

                input("Pressione ENTER para começar: ")

                while hp_monstro > 0 and hp > 0 and not game_over:

                    dano = random.randint(1, 6)
                    sorte = random.randint(1, 10)

                    print("\nAtaque do monstro")
                    input("Pressione ENTER para a ação.")

                    if sorte % 2 == 0:

                        print(f"Valor sorteado: {sorte}")
                        print("Ataque do monstro concluído.")
                        print(f"Dano: {dano}")
                        hp -= dano
                        print(f"Sua HP: {hp}")

                    else:

                        print(f"Valor sorteado: {sorte}")
                        print("Ataque do monstro falhou.")

                    if hp <= 0:

                        print("Você não aguentou os ataques do monstro guardião do poder...")
                        print(f"HP: {hp}")
                        game_over = True

                    if hp_monstro <= 0:

                        print("Você derrotou o monstro! Conquistou o colar sagrado!")
                        print("Ao terminar a luta você finalmente pode ter acesso ao antigo artefato que virou uma lenda.")
                        print("Você pega o colar, guarda, e agora pode seguir sua viagem de volta.")
                        game_over = True

                    if hp > 0 and not game_over:

                        dano = random.randint(1, 4)
                        sorte = random.randint(1, 6)

                        print(f"\nAtaque de {nome}:")

                        input("Pressione ENTER para atacar.")

                        if sorte % 2 == 0:

                            print(f"Valor sorteado: {sorte}")
                            print(f"Dano: {dano}")
                            hp_monstro -= dano
                            print(f"HP do monstro: {hp_monstro}")

                        else:
                            print(f"Valor sorteado: {sorte}")
                            print("Seu ataque falhou.")

            else:
                print("Você foge do monstro e a missão falha.")
                game_over = True

        else:
            print("Resposta incorreta, a resposta era 'Nome'.")
            print("Um braço surge de dentro do baú e puxa você para dentro.")
            print("GAME OVER")
            game_over = True

    else:
        print("Você ignora o baú, mas sente que perdeu sua chance de encontrar o artefato.")
        print("GAME OVER")
        game_over = True

print("\nFim da aventura.")
