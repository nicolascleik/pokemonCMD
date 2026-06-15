import random
import time
from models.estabelecimento import Estabelecimento

class Cassino(Estabelecimento):
    """
    Classe filha que representa o cassino.
    Permite utilizar da sorte e dinheiro para ganhar premios ou perder tudo!
    """
    def __init__(self):
        super().__init__("Cassino", tempo_de_ir=2)

    def rodar_cassino(self, player):
        while True:
            print("\n" + "777 " * 5)
            print("      BEM-VINDO AO CASSINO ROCKET!      ")
            print("  Onde seus sonhos podem se realizar...  ")
            print("          (ou sua carteira esvaziar)     ")
            print("777 " * 5)
            print(f"Seu Saldo Atual: ${player.get_dinheiro():.2f}")
            print("-" * 30)
            print("1 - Caca-Niquel Pokemon (Custa $10)")
            print("2 - Adivinhe o Numero (Aposta Customizada)")
            print("0 - Sair do Cassino")
            print("-" * 30)

            escolha = input("Escolha sua sorte: ")

            if escolha == "1":
                self.jogar_caca_niquel(player)
            elif escolha == "2":
                self.jogar_adivinhacao(player)
            elif escolha == "0":
                print("\nObrigado por doar seu dinheiro... digo, volte sempre!")
                break
            else:
                print("Opcao invalida!")

    def jogar_caca_niquel(self, player):
        custo = 10.0
        if player.get_dinheiro() < custo:
            print("\nVoce nao tem dinheiro suficiente para puxar a alavanca!")
            return

        player.alterar_dinheiro(-custo)
        icones = ["ELE", "FOG", "AGU", "PLA", "EST", "MOR"]
        
        print("\nGirando a maquina...")
        time.sleep(0.5)
        
        resultado = [random.choice(icones) for _ in range(3)]
        print(f"| {resultado[0]} | {resultado[1]} | {resultado[2]} |")
        
        if resultado[0] == resultado[1] == resultado[2]:
            if resultado[0] == "EST":
                premio = 200.0
                print(f"JACKPOT! TRES ESTRELAS! Voce ganhou ${premio}!")
            else:
                premio = 50.0
                print(f"TRINCA! Voce ganhou ${premio}!")
            player.alterar_dinheiro(premio)
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = 15.0
            print(f"Par! Voce recuperou seu dinheiro e ganhou um extra de ${premio - custo:.2f}!")
            player.alterar_dinheiro(premio)
        else:
            print("Que pena! Tente novamente.")

    def jogar_adivinhacao(self, player):
        print("\n--- ADIVINHE O POKEMON ---")
        print("Pensei em um numero de 1 a 10.")
        
        try:
            aposta = float(input(f"Quanto deseja apostar? (Saldo: ${player.get_dinheiro():.2f}): $"))
            if aposta <= 0 or aposta > player.get_dinheiro():
                print("Valor de aposta invalido!")
                return
        except ValueError:
            print("Digite um valor numerico!")
            return

        try:
            chute = int(input("Qual o seu palpite (1-10)? "))
            if chute < 1 or chute > 10:
                print("Numero fora do intervalo!")
                return
        except ValueError:
            print("Digite um numero inteiro!")
            return

        secreto = random.randint(1, 10)
        player.alterar_dinheiro(-aposta)
        
        print(f"\nO numero secreto era... {secreto}!")
        
        if chute == secreto:
            ganho = aposta * 5
            print(f"ACERTOU EM CHEIO! Voce ganhou 5x sua aposta: ${ganho:.2f}!")
            player.alterar_dinheiro(ganho)
        elif abs(chute - secreto) == 1:
            ganho = aposta * 1.5
            print(f"QUASE! Por ser tao perto, voce ganhou 1.5x sua aposta: ${ganho:.2f}!")
            player.alterar_dinheiro(ganho)
        else:
            print("Errou longe! A Equipe Rocket agradece a doacao.")
