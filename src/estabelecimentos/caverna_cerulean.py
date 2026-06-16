import random
from models.estabelecimento import Estabelecimento
from models.batalha import Batalha

from pokemons_comuns.pikachu import Pikachu
from pokemons_comuns.charmander import Charmander
from pokemons_comuns.bulbasaur import Bulbasaur
from pokemons_comuns.eevee import Eevee
from pokemons_comuns.meowth import Meowth
from pokemons_comuns.venonat import Venonat
from pokemons_comuns.butterfree import Butterfree
from pokemons_comuns.gengar import Gengar
from pokemons_comuns.mew import Mew
from pokemons_comuns.mimikyu import Mimikyu
from pokemons_comuns.snorlax import Snorlax
from pokemons_comuns.charizard import Charizard
from pokemons_comuns.jigglypuff import Jigglypuff
from pokemons_comuns.haunter import Haunter
from pokemons_comuns.chikoritta import Chikoritta

from pokemons_lendarios.mewtwo import Mewtwo
from pokemons_lendarios.articuno import Articuno
from pokemons_lendarios.dialga import Dialga
from pokemons_lendarios.lugia import Lugia
from pokemons_lendarios.mesprit import Mesprit
from pokemons_lendarios.rayquaza import Rayquaza


class CavernaCerulean(Estabelecimento):
    """
    Classe filha que representa a Caverna.
    Respeita o contrato de Estabelecimento e consome recursos por busca.
    """

    def __init__(self):
        super().__init__("Caverna Cerulean", tempo_de_ir=4)

        self.comuns = [
            Pikachu, Charmander, Bulbasaur,
            Eevee, Meowth, Venonat, Butterfree,
            Gengar, Mew, Mimikyu, Snorlax,
            Charizard, Jigglypuff, Haunter, Chikoritta
        ]

        self.lendarios = [
            Mewtwo, Articuno, Dialga,
            Lugia, Mesprit, Rayquaza
        ]

    def interagir(self, jogador, relogio) -> None:
        while True:
            print("\n" + "T " * 15)
            print("      CAVERRNA CERULEAN      ")
            print("T " * 15)
            print("1 - Procurar Pokémon Selvagem (Gasta 3h e 25 Energia)")
            print("0 - Sair da Caverna")

            escolha = input("\nO que deseja fazer? ")

            if escolha == "0":
                print("Saindo da caverna...")
                break

            elif escolha == "1":
                if relogio.hora_atual + 3 >= 24:
                    print("Está ficando muito tarde para explorar esse local escuro. Melhor ir embora!")
                    continue
                if jogador.energia_atual <= 25:
                    print("Você está com muita fome para procurar Pokémons agora.")
                    continue

                relogio.avancar_tempo(3)
                jogador.gastar_energia(25)
                print(
                    f"\nVocê caminha silenciosamente... (Hora: {relogio.hora_atual}h | Energia: {jogador.energia_atual})")

                sorteio = random.random()

                if sorteio <= 0.20:
                    # 20% de chance de vir nada (0.00 até 0.20)
                    print("Nada além de pedras por aqui.")
                    input("Pressione Enter para continuar...")

                elif sorteio <= 0.30:
                    # 10% de chance de Lendário (0.20 até 0.30)
                    print("\nO AR ESTÁ FICANDO PESADO... ALGO PODEROSO SE APROXIMA!")
                    pkm_classe = random.choice(self.lendarios)

                    batalha = Batalha(jogador, pkm_classe())
                    venceu_ou_fugiu = batalha.iniciar()

                    if not venceu_ou_fugiu:
                        return  # Sai da carverna e volta pro main.py se o jogador desmaiar

                else:
                    # 70% de chance de Comum (0.30 até 1.00)
                    pkm_classe = random.choice(self.comuns)
                    print("\nUm Pokémon selvagem saiu do escuro!")

                    batalha = Batalha(jogador, pkm_classe())
                    venceu_ou_fugiu = batalha.iniciar()

                    if not venceu_ou_fugiu:
                        return  # Sai da carverna e volta pro main.py se o jogador desmaiar
            else:
                print("Opção inválida!")
