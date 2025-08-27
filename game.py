import random

nome = str(input("Olá, bem-vindo ao Simyanin Sirri!\nDigite seu nickname: "))

classes = {
    '1': "Fogo",
    '2': "Água",
    '3': "Terra",
}

print("\nConheça as classes de dominadores de elementos:")
print("1 - Fogo (plus de dano)")
print("2 - Água (plus de HP)")
print("3 - Terra (escudo para lutas)")

classe_num = input(f"{nome}, escolha qual será seu elemento: ")
classe_nome = classes.get(classe_num, "Fogo")

hp = 12
game_over = False
escudo = 0
bonus_dano = 0

if classe_num == "1": 
    bonus_dano = 3
elif classe_num == "2":
    hp += 3
elif classe_num == "3":
    escudo = 3

print(f"\nGrande {nome}, o dominador de {classe_nome}!")
print("\n---------------- Em busca da Pedra Filosofal de Simya, o reino perdido ----------------\n")
input("Pressione ENTER para continuar...")

print("\nNas terras esquecidas de Simya, conta-se sobre uma Pedra Filosofal.")
print("Uma lendária substância da alquimia que se acreditava ter o poder de transmutar metais básicos em ouro e produzir o Elixir da Vida, concedendo imortalidade.")
print("Conta a lenda que ela está protegida nas ruínas de um antigo castelo.")
print("Dizem que apenas os mais corajosos conseguem atravessar as armadilhas, monstros e enigmas que protegem o artefato sagrado.")
print(f"Agora, o destino recai sobre você, {nome}, o valente dominador de {classe_nome}, que parte em busca dessa relíquia lendária.")

while hp > 0 and not game_over:

    print("\nDepois de andar por 4 dias com o auxílio de uma mapa mágico, você chega na antiga Simya. Diante de você, duas entradas:\n")
    print("1 - O PORTÃO PRINCIPAL, parcialmente destruído e enferrujado, levemente iluminado pela lua.")
    print("2 - UM TÚNEL LATERAL, escuro e estreito, de onde ecoam estranhos sons.")
    print("3 - FUGIR.")

    escolha = int(input("Você percebe que precisa escolher entre elas duas, e sua decisão é: "))

    if escolha == 1:
        print("\nÉ decidido entrar pelo portão principal.")
        print("Você encontra em frente dois esqueletos GIGANTES com espadas em chamas que bloqueiam sua passagem.")
        print("1 - ATACAR")
        print("2 - DEFENDER")
        print("3 - FUGIR")

        acao = int(input(f"O que você, {nome}, decide fazer?: "))

        if acao == 1:
            print("\nArduamente você consegue derrota-los e entrar no reino.")
            print("Mas os contra-ataques foram dolorosos, e precisamos saber o seu estado físico.")
            input("\nPressione ENTER para rodar o dado...")
            dado = random.randint(1, 6)
            print(f"\nValor do dado: {dado}\n")
            if dado in range(1, 4):
                print("Você não conseguiu desviar de alguns conta-ataques dos esqueletos e perde -2 de HP")
                hp -= 2
            else:
                print("Você lutou muito bem contra os esqueletos e não perdeu nada de HP!")
            print(f"HP: {hp}")

        elif acao == 2:
            print("\nVocê consegue se defender muito bem e conseguiu correr dos esqueletos.")
            print("Vamos descobrir se durante sua fuga não houveram complicações.") 
            input("\nPressione ENTER para rodar o dado...")
            dado = random.randint(1, 6)
            print(f"\nValor do dado: {dado}\n")
            if dado in range(1, 4):
                print("Enquanto você corria para evitar uma luta, você tropeçou em um dos inúmeros destroços pelo caminho. (-1 HP)")
                hp -= 1
            else:
                print("Você correu super rápido e com muita sorte desviou de obstáculos próximos. (Não perdeu HP)")
            print(f"HP: {hp}")
        else:
            print("\nVocê percebe o quão grande são os esqueletos e quão afiada são suas espadas.")
            print("Dessa forma, você decide fugir e desiste da missão.")
            print("GAME OVER")
            game_over = True

    elif escolha == 2:
        print("\nVocê decide entrar pelo túnel.")
        print("Ao chão, você encontra um pergaminho brilhando em dourado e é tomado por uma curiosidade imensa.")
        valor_pergaminho = int(input("\nDigite um número de 1 a 10: "))
        if valor_pergaminho % 2 == 0:
            print("O pergaminho brilha em verde e ele te dá +3 de HP!")
            hp += 3
        else:
            print("O pergaminho brilha em vermelho e explode na sua mão, e assim você perde -1 de HP")
            hp -= 1
        print(f"HP: {hp}")
    else:
        print("\nVocê decide fugir e desiste da missão...")
        print("GAME OVER")
        game_over = True

    if hp <= 0 or game_over:
        break

    input("\nPressione ENTER para continuar...")
    print("\nAo entrar no reino de Symya, você encontra um armazém antigo e decide entrar.")
    print("Dentro dele, há um espelho em uma parede. Você percebe que de alguma forma ele está sussurrando: 'Escolha sua verdade, e o caminho será revelado.'")
    print("\n1 - Você olha seu reflexo pelo espelho.")
    print("2 - Você ignora o espelho e foca na missão.")

    escolha = int(input(f"O que você, {nome}, decide fazer?: "))

    if escolha == 1:
        print("\nAo se olhar pelo reflexo, percebe que aquilo era uma armadilha mágica e fica totalmente atordoado.")
        print("O espelho diz para você adivinhar um número entre 1 a 6, caso erre, perderá um número aleatório de HP.")
        print("Você tem 3 tentativas.")

        num_secreto = random.randint(1, 6)
        tentativas = 3
        adivinha_num = 0

        while adivinha_num != num_secreto and tentativas > 0:
            adivinha_num = int(input("\nAdivinhe o número entre 1 a 6: "))
            tentativas -= 1
            if adivinha_num == num_secreto:
                print("\nParabéns! Você acertou o número!")
                print("Você consegue escapar e sai intacto!!")
            else:
                if tentativas > 0:
                    print(f"\nErrado! Nova chance. Você ainda tem {tentativas} tentativas.")
                else:
                    dano = random.randint(1, 3)
                    print("\nVocê errou!")
                    print(f"O número era {num_secreto}.")
                    print(f"Você perdeu {dano} de HP.")
                    hp -= dano
                    print(f"HP: {hp}")

    elif escolha == 2:
        print("\nComo você é bem treinado, conhece técnicas malígnas e imagina que possa ser uma armadilha e decide ignorar o espelho e continuar a missão.")
        print("+1 de HP por autoconfiança.")
        hp += 1
        print(f"HP: {hp}")
    else:
        print("\nVocê sente um medo muito grande e decide fugir...")
        print("GAME OVER")
        game_over = True

    if hp <= 0 or game_over:
        break

    print("\nDepois de sair do armazém, você finalmente chega no castelo e encontra um baú de madeira em um santuário com estátuas ao seu redor.")
    print("1 - Você decide abrir")
    print("2 - Você ignora o baú")

    escolha = int(input(f"O que você, {nome}, decide fazer?: "))

    if escolha == 1:
        print("\nAo abrir o baú, surge um rosto feito de vapor e ele te diz: ")
        print("'Ao abrir o baú, a charada deve acertar e se errar o preço deve pagar!'")
        print("'Sou duro e silencioso, não falo nem caminho. Posso estar sozinho ou fazer parte de um caminho. Quem sou eu?'")

        resposta_charada = "Pedra"
        resposta_usuario = input("Digite sua resposta: ")
        
        if resposta_charada.casefold() == resposta_usuario.casefold(): 
            print("\nCERTA RESPOSTA!!")
            print("O vapor começa a sumir e do baú sai um monstro de pedra com metros de altura usando um colar com um pingente de uma pedra brilhante.")
            print("Ao ver o colar no pescoço dele, você percebe que aquele é o artefato que armazena o poder que você estava à procura.")
            print("A PEDRA FILOSOFAL")
            print("1 - Lutar")
            print("2 - Fugir")

            escolha = int(input(f"\nO que você, {nome}, decide fazer?: "))

            if escolha == 1:
                hp_monstro = 15
                print("\nOs seus ataques e do inimigo serão feitos através de sorte.")
                print("Será gerado um número, se for PAR o ataque é concluído.")
                print("Se for ÍMPAR, o ataque falha.")
                print(f"Os danos de ambos ({nome} e Monstro) são aleatórios de 1 a 6.")
                input("\nPressione ENTER para começar:")

                while hp_monstro > 0 and hp > 0 and not game_over:
                    # Ataque do monstro
                    dano_monstro = random.randint(1, 6)
                    sorte_monstro = random.randint(1, 10)

                    print("\nAtaque do monstro")
                    input("Pressione ENTER para a ação.")

                    if sorte_monstro % 2 == 0:
                        dano_final_monstro = max(0, dano_monstro - escudo)
                        print(f"Valor sorteado: {sorte_monstro}")
                        print("Ataque do monstro concluído.")

                        if escudo > 0:
                            print(f"Escudo: {escudo} | Dano do Monstro: {dano_monstro} -> Dano recebido: {dano_final_monstro}")

                        print(f"Dano: {dano_final_monstro}")
                        hp -= dano_final_monstro
                        print(f"Sua HP: {hp}")
                    else:
                        print(f"Valor sorteado: {sorte_monstro}")
                        print("Ataque do monstro falhou.")

                    if hp <= 0:
                        print("\nVocê não aguentou os ataques do monstro guardião do poder e infelizmente morre...")
                        game_over = True
                        break

                    # Ataque do jogador
                    if hp_monstro > 0:
                        dano = random.randint(1, 6) + bonus_dano
                        sorte = random.randint(1, 10)

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

                    if hp_monstro <= 0:
                        print("\nVocê derrotou o monstro! Conquistou a pedra sagrada!")
                        print("Ao derrotar o monstro e pegar o colar com a pedra, o reino junto ao castelo treme e começa a desabar.")
                        print("Você percebe que o que mantia o local em pé era o pdoerr do colar!")
                        print("Mas nada disso importa, a Pedra Filosofal foi encontrada!")
                        game_over = True
                        break

            else:
                print("\nVocê foge do monstro e a missão falha.")
                game_over = True

        else:
            print("\nResposta incorreta, a resposta era 'Pedra'.")
            print("Um braço feito de pedra surge de dentro do baú e puxa você para dentro.")
            print("Você Morreu!")
            print("GAME OVER")
            game_over = True

    else:
        print("\nVocê ignora o baú e passa o resto da sua vida em busca da Pedra Filosofal.")
        print("GAME OVER")
        game_over = True

print("\nFim da aventura.")
