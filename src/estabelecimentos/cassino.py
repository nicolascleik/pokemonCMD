import random
import time
from models.estabelecimento import Estabelecimento


class Cassino(Estabelecimento):
    """
    Classe filha que representa o cassino.
    Permite utilizar da sorte e dinheiro para ganhar prêmios ou perder tudo!
    """

    def __init__(self):
        super().__init__("Cassino Rocket", tempo_de_ir=2)

    def interagir(self, jogador, relogio) -> None:
        while True:
            print("\n" + "777 " * 5)
            print("      BEM-VINDO AO CASSINO ROCKET!      ")
            print("  Onde seus sonhos podem se realizar...  ")
            print("          (ou sua carteira esvaziar)     ")
            print("777 " * 5)
            print(f"Seu Saldo Atual: ${jogador.dinheiro:.2f}")
            print(f"Hora atual: {relogio.hora_atual}h | Energia: {jogador.energia_atual}")
            print("-" * 30)
            print("1 - Caça-Níquel Pokémon (Aposta Fixa: $10)")
            print("2 - Adivinhe o Número (Aposta Customizada)")
            print("3 - Mesa de Blackjack / 21 (Aposta Customizada)")
            print("0 - Sair do Cassino")
            print("-" * 30)

            escolha = input("Escolha sua sorte: ")

            if escolha == "0":
                print("\nObrigado por doar seu dinheiro... digo, volte sempre!")
                break

            # --- Validação de Tempo e Energia para jogar ---
            # Vamos cobrar 1 hora e 5 de energia por rodada de qualquer jogo
            # para evitar que o jogador fique farmando infinitamente.
            if relogio.hora_atual + 1 >= 24:
                print("\n[Segurança] 'O cassino está fechando, vá para casa!'")
                break
            if jogador.energia_atual <= 5:
                print("\n[Segurança] 'Você mal consegue ficar em pé. Vá comer algo antes de jogar.'")
                continue

            # Consome os recursos da rodada
            relogio.avancar_tempo(1)
            jogador.gastar_energia(5)

            # Roteamento dos jogos
            if escolha == "1":
                self._jogar_caca_niquel(jogador)
            elif escolha == "2":
                self._jogar_adivinhacao(jogador)
            elif escolha == "3":
                self._jogar_blackjack(jogador)
            else:
                print("Opção inválida!")

    # Métodos internos dos jogos (prefixo '_' indica que são privados à classe)

    def _jogar_caca_niquel(self, jogador) -> None:
        custo = 10.0
        if jogador.dinheiro < custo:
            print("\nVocê não tem dinheiro suficiente para puxar a alavanca!")
            return

        jogador.modificar_dinheiro(-custo)
        icones = ["ELE", "FOG", "AGU", "PLA", "EST", "MOR"]

        print("\nGirando a máquina...")
        time.sleep(0.5)

        resultado = [random.choice(icones) for _ in range(3)]
        print(f"| {resultado[0]} | {resultado[1]} | {resultado[2]} |")

        if resultado[0] == resultado[1] == resultado[2]:
            if resultado[0] == "EST":
                premio = 200.0
                print(f"JACKPOT! TRÊS ESTRELAS! Você ganhou ${premio:.2f}!")
            else:
                premio = 50.0
                print(f"TRINCA! Você ganhou ${premio:.2f}!")
            jogador.modificar_dinheiro(premio)

        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = 15.0
            print(f"Par! Você recuperou seu dinheiro e ganhou um extra de ${(premio - custo):.2f}!")
            jogador.modificar_dinheiro(premio)
        else:
            print("Que pena! Tente novamente.")

    def _jogar_adivinhacao(self, jogador) -> None:
        print("\n--- ADIVINHE O NÚMERO ---")
        try:
            aposta = float(input(f"Quanto deseja apostar? (Saldo: ${jogador.dinheiro:.2f}): $"))
            if aposta <= 0 or aposta > jogador.dinheiro:
                print("Valor de aposta inválido ou saldo insuficiente!")
                return

            chute = int(input("Qual o seu palpite (1-10)? "))
            if chute < 1 or chute > 10:
                print("Número fora do intervalo!")
                return
        except ValueError:
            print("Entrada inválida. Digite apenas números!")
            return

        secreto = random.randint(1, 10)
        jogador.modificar_dinheiro(-aposta)

        print(f"\nO número secreto era... {secreto}!")

        if chute == secreto:
            ganho = aposta * 5
            print(f"ACERTOU EM CHEIO! Você ganhou 5x sua aposta: ${ganho:.2f}!")
            jogador.modificar_dinheiro(ganho)
        elif abs(chute - secreto) == 1:
            ganho = aposta * 1.5
            print(f"QUASE! Por ser tão perto, você ganhou 1.5x sua aposta: ${ganho:.2f}!")
            jogador.modificar_dinheiro(ganho)
        else:
            print("Errou longe! A Equipe Rocket agradece a doação.")

    def _jogar_blackjack(self, jogador) -> None:
        print("\n--- MESA DE BLACKJACK (21) ---")

        try:
            aposta = float(input(f"Quanto deseja apostar? (Saldo: ${jogador.dinheiro:.2f}): $"))
            if aposta <= 0 or aposta > jogador.dinheiro:
                print("Valor de aposta inválido ou saldo insuficiente!")
                return
        except ValueError:
            print("Entrada inválida. Digite apenas números!")
            return

        jogador.modificar_dinheiro(-aposta)
        print(f"\nAposta de ${aposta:.2f} confirmada. O Dealer começa a distribuir as cartas...\n")
        time.sleep(1)

        # Baralho: As cartas J, Q e K valem 10. O Ás (11) tem uma lógica especial.
        cartas_possiveis = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        def calcular_mao(mao):
            total = sum(mao)
            ases = mao.count(11)
            # Se o total passar de 21 e tivermos um Ás, o Ás passa a valer 1 (reduz 10)
            while total > 21 and ases > 0:
                total -= 10
                ases -= 1
            return total

        mao_jogador = [random.choice(cartas_possiveis), random.choice(cartas_possiveis)]
        mao_dealer = [random.choice(cartas_possiveis), random.choice(cartas_possiveis)]

        print(f"Suas cartas: {mao_jogador} -> Total: {calcular_mao(mao_jogador)}")
        print(f"Cartas do Dealer: [{mao_dealer[0]}, ?]")

        while True:
            total_jogador = calcular_mao(mao_jogador)

            if total_jogador == 21:
                print("\n[Dealer] 'Você conseguiu um 21!'")
                break

            escolha = input("\nDeseja (1) Comprar carta ou (2) Parar? ")

            if escolha == "1":
                nova_carta = random.choice(cartas_possiveis)
                mao_jogador.append(nova_carta)
                total_jogador = calcular_mao(mao_jogador)

                print(f"\nVocê comprou um {nova_carta}.")
                print(f"Suas cartas: {mao_jogador} -> Total: {total_jogador}")

                if total_jogador > 21:
                    print("\n💥 ESTOUROU! Você passou de 21. O Dealer limpa a mesa e recolhe suas fichas.")
                    return  # O método morre aqui, a aposta já foi descontada no passo 2

            elif escolha == "2":
                print("\nVocê decidiu parar.")
                break
            else:
                print("Opção inválida!")

        print("\n" + "-" * 30)
        print("TURNO DO DEALER")
        print("-" * 30)
        total_dealer = calcular_mao(mao_dealer)
        print(f"O Dealer revela a carta oculta: {mao_dealer[1]}")
        print(f"Cartas do Dealer: {mao_dealer} -> Total: {total_dealer}")
        time.sleep(1)

        while total_dealer < 17:
            nova_carta = random.choice(cartas_possiveis)
            mao_dealer.append(nova_carta)
            total_dealer = calcular_mao(mao_dealer)

            print(f"\nO Dealer compra um {nova_carta}.")
            print(f"Cartas do Dealer: {mao_dealer} -> Total: {total_dealer}")
            time.sleep(1)

        print("\n--- RESULTADO FINAL ---")
        time.sleep(1)

        if total_dealer > 21:
            print(f"💥 O DEALER ESTOUROU! Você venceu e recebeu ${aposta * 2:.2f}!")
            jogador.modificar_dinheiro(aposta * 2)

        elif total_jogador > total_dealer:
            print(f"🏆 VOCÊ VENCEU O DEALER! Você recebeu ${aposta * 2:.2f}!")
            jogador.modificar_dinheiro(aposta * 2)

        elif total_jogador == total_dealer:
            print("🤝 EMPATE (Push)! Ninguém ganha, a sua aposta foi devolvida.")
            jogador.modificar_dinheiro(aposta)

        else:
            print("💸 O DEALER VENCEU! A Casa sempre ganha.")