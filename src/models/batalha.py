import random
import time
import copy


class Batalha:
    """
    Classe que gerencia a lógica de uma batalha entre o jogador e um Pokémon selvagem.
    Orquestra os turnos e a interação entre os objetos, respeitando o encapsulamento.
    """

    def __init__(self, player, wild_pokemon, fuga_bloqueada: bool = False):
        self._player = player
        self._wild_pokemon = wild_pokemon
        self._fuga_bloqueada = fuga_bloqueada

        # Pega o primeiro Pokémon vivo da equipe, se houver
        self._player_pokemon = None
        if self._player.obter_equipe():
            self._player_pokemon = self._player.obter_equipe()[0]

    def iniciar(self) -> bool:
        if not self._player_pokemon:
            print("\nVocê não tem Pokémons na equipe para batalhar!")
            return False

        if self._player_pokemon.vida_atual <= 0:
            print(f"\n{self._player_pokemon.nome} está desmaiado! Vá ao Hospital ou use uma Poção.")
            return False

        print("\n" + "X" * 20)
        print(f"UM {self._wild_pokemon.nome} SELVAGEM APARECEU!")
        print("X" * 20)
        print(self._wild_pokemon.arte_ascii)

        while self._wild_pokemon.vida_atual > 0 and self._player_pokemon.vida_atual > 0:
            print(
                f"\n--- {self._player_pokemon.nome} ({self._player_pokemon.vida_atual}/{self._player_pokemon.hp_maximo}) vs {self._wild_pokemon.nome} ({self._wild_pokemon.vida_atual}/{self._wild_pokemon.hp_maximo}) ---")
            print("1 - Atacar")
            print("2 - Usar Pokébola")
            print("3 - Fugir")

            escolha = input("O que deseja fazer? ")

            if escolha == "1":
                # Turno do Jogador
                self._player_pokemon.atacar(self._wild_pokemon)
                time.sleep(1)

                if self._wild_pokemon.vida_atual <= 0:
                    print(f"\nO {self._wild_pokemon.nome} selvagem desmaiou!")
                    recompensa = random.randint(10, 30)
                    self._player.modificar_dinheiro(recompensa)
                    print(f"Você ganhou ${recompensa:.2f} pela vitória!")
                    return True

                # Turno do Selvagem
                self._wild_pokemon.atacar(self._player_pokemon)
                time.sleep(1)

                if self._player_pokemon.vida_atual <= 0:
                    print(f"\nSeu {self._player_pokemon.nome} desmaiou!")
                    return False


            elif escolha == "2":

                if self._fuga_bloqueada:
                    print(f"\n[Juiz/Cobrador] É proibido capturar Pokémons nesta batalha!")
                    continue

                # Se não está bloqueada, tenta a captura
                if self.tentar_capturar():
                    return True

                # Se falhar, toma ataque
                print(f"O {self._wild_pokemon.nome} selvagem aproveita sua falha para atacar!")

                self._wild_pokemon.atacar(self._player_pokemon)

                if self._player_pokemon.vida_atual <= 0:
                    print(f"\nSeu {self._player_pokemon.nome} desmaiou!")
                    return False


            elif escolha == "3":
                if self._fuga_bloqueada:
                    print(f"\n[Juiz/Cobrador] Não há para onde fugir! Lute até o fim!")
                    self._wild_pokemon.atacar(self._player_pokemon)
                    time.sleep(1)
                    if self._player_pokemon.vida_atual <= 0:
                        print(f"\nSeu {self._player_pokemon.nome} desmaiou!")
                        return False

                    continue

                if self._player.tentar_fugir():
                    return True

                print(f"O {self._wild_pokemon.nome} selvagem bloqueia sua fuga e ataca!")
                self._wild_pokemon.atacar(self._player_pokemon)

                if self._player_pokemon.vida_atual <= 0:
                    print(f"\nSeu {self._player_pokemon.nome} desmaiou!")

                    return False
            else:
                print("Escolha inválida!")

        return True

    def tentar_capturar(self) -> bool:
        if not self._player.possui_item("POKEBOLA"):
            print("\nVocê não tem Pokébolas!")
            return False

        self._player.consumir_item("POKEBOLA")
        print(f"\nVocê lançou uma Pokébola em {self._wild_pokemon.nome}!")

        if self._wild_pokemon.raridade == "LENDARIO":
            chance_base = 0.10
        else:
            chance_base = 0.50

        vida_relativa = self._wild_pokemon.vida_atual / self._wild_pokemon.hp_maximo
        chance_final = chance_base + (1.0 - vida_relativa) * 0.30

        print("Balançando...")
        time.sleep(1)

        if random.random() < chance_final:
            print(f"GOTCHA! O {self._wild_pokemon.nome} foi capturado!")

            pokemon_capturado = copy.deepcopy(self._wild_pokemon)
            pokemon_capturado.curar()

            self._player.adicionar_pokemon(pokemon_capturado)
            return True
        else:
            print(f"Ah não! O {self._wild_pokemon.nome} escapou da Pokébola!")
            return False