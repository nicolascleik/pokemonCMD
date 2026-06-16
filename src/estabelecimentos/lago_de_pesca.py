import random
from models.estabelecimento import Estabelecimento
from models.batalha import Batalha

from pokemons_comuns.squirtle import Squirtle
from pokemons_comuns.blastoise import Blastoise
from pokemons_comuns.slowpoke import Slowpoke
from pokemons_lendarios.kyogre import Kyogre


class LagoDePesca(Estabelecimento):
    """
    Classe filha que representa o Lago de Pesca.
    Permite pescar itens valiosos ou encontrar Pokémons aquáticos.
    """

    def __init__(self):
        super().__init__("Lago de Pesca", tempo_de_ir=2)

        self.comuns = [Squirtle, Blastoise, Slowpoke]
        self.lendarios = [Kyogre]

    def interagir(self, jogador, relogio) -> None:
        while True:
            print("\n" + "~ " * 15)
            print("         LAGO DE PESCA         ")
            print("~ " * 15)
            print("1 - Jogar a vara de pescar (Gasta 2h e 15 Energia)")
            print("0 - Voltar para a cidade")

            escolha = input("\nO que deseja fazer? ")

            if escolha == "0":
                print("Guardando a vara de pescar...")
                break

            elif escolha == "1":
                # 1. Validação de Recursos
                if relogio.hora_atual + 2 >= 24:
                    print("Está muito escuro para ver a boia. Melhor ir embora!")
                    continue
                if jogador.energia_atual <= 15:
                    print("Você não tem força para puxar a vara. Vá comer algo!")
                    continue

                # 2. Consumo de Recursos
                relogio.avancar_tempo(2)
                jogador.gastar_energia(15)
                print(
                    f"\nVocê joga a isca e espera... (Hora: {relogio.hora_atual}h | Energia: {jogador.energia_atual})")

                # 3. Matemática do Sorteio (RNG)
                sorteio = random.random()

                if sorteio <= 0.30:
                    # 30% de chance de não pescar nada
                    print("Um sapato velho... Nada de útil por aqui.")
                    input("Pressione Enter para continuar...")

                elif sorteio <= 0.60:
                    # 30% de chance de pescar um Peixe (0.30 a 0.60)
                    print("A boia afundou! Você puxou um PEIXE enorme!")
                    jogador.adicionar_item("PEIXE", 1)
                    input("Pressione Enter para continuar...")

                elif sorteio <= 0.65:
                    # 5% de chance do Lendário das Águas (0.60 a 0.65)
                    print("\nA ÁGUA COMEÇA A FERVER E UM REDEMOINHO SE FORMA!")
                    batalha = Batalha(jogador, Kyogre())
                    if not batalha.iniciar():
                        return
                else:
                    # 35% de chance de Pokémon Comum de Água (0.65 a 1.00)
                    pkm_classe = random.choice(self.comuns)
                    print("\nUm Pokémon fisgou a isca e saltou da água!")
                    batalha = Batalha(jogador, pkm_classe())
                    if not batalha.iniciar():
                        return
            else:
                print("Opção inválida!")