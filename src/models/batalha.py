import random
import time

class Batalha:
    """
    Classe que gerencia a logica de uma batalha entre o jogador e um Pokemon selvagem.
    """
    def __init__(self, player, wild_pokemon):
        self.player = player
        self.wild_pokemon = wild_pokemon
        self.player_pokemon = player.equipe[0] if player.equipe else None

    def iniciar(self):
        if not self.player_pokemon:
            print("\nVoce nao tem Pokemons para batalhar!")
            return False

        if self.player_pokemon.get_vida_atual() <= 0:
            print(f"\n{self.player_pokemon.nome} esta desmaiado! Va ao Hospital ou use uma Pocao.")
            return False

        print("\n" + "X" * 20)
        print(f"UM {self.wild_pokemon.nome} SELVAGEM APARECEU!")
        print("X" * 20)
        print(self.wild_pokemon.arte_ascii)
        
        while self.wild_pokemon.get_vida_atual() > 0 and self.player_pokemon.get_vida_atual() > 0:
            print(f"\n--- {self.player_pokemon.nome} ({self.player_pokemon.get_vida_atual()}/{self.player_pokemon.hp_maximo}) vs {self.wild_pokemon.nome} ({self.wild_pokemon.get_vida_atual()}/{self.wild_pokemon.hp_maximo}) ---")
            print("1 - Atacar")
            print("2 - Usar Pokebola")
            print("3 - Fugir")
            
            escolha = input("O que deseja fazer? ")

            if escolha == "1":
                # Turno do Jogador
                self.player_pokemon.atacar(self.wild_pokemon)
                time.sleep(1)
                
                if self.wild_pokemon.get_vida_atual() <= 0:
                    print(f"\nO {self.wild_pokemon.nome} selvagem desmaiou!")
                    recompensa = random.randint(10, 30)
                    self.player.alterar_dinheiro(recompensa)
                    print(f"Voce ganhou ${recompensa} pela vitoria!")
                    return True

                # Turno do Selvagem
                self.wild_pokemon.atacar(self.player_pokemon)
                time.sleep(1)
                
                if self.player_pokemon.get_vida_atual() <= 0:
                    print(f"\nSeu {self.player_pokemon.nome} desmaiou!")
                    return False

            elif escolha == "2":
                if self.tentar_capturar():
                    return True
                
                # Se falhar na captura, o selvagem ataca
                print(f"O {self.wild_pokemon.nome} selvagem aproveita sua falha para atacar!")
                self.wild_pokemon.atacar(self.player_pokemon)
                if self.player_pokemon.get_vida_atual() <= 0:
                    print(f"\nSeu {self.player_pokemon.nome} desmaiou!")
                    return False

            elif escolha == "3":
                if self.player.tentar_fugir():
                    return True
                
                # Se falhar na fuga, o selvagem ataca
                print(f"O {self.wild_pokemon.nome} selvagem bloqueia sua fuga e ataca!")
                self.wild_pokemon.atacar(self.player_pokemon)
                if self.player_pokemon.get_vida_atual() <= 0:
                    print(f"\nSeu {self.player_pokemon.nome} desmaiou!")
                    return False
            else:
                print("Escolha invalida!")

        return True

    def tentar_capturar(self):
        if "Pokebola" not in self.player.inventario or self.player.inventario["Pokebola"] <= 0:
            print("\nVoce nao tem Pokebolas!")
            return False

        self.player.usar_item("Pokebola")
        print(f"\nVoce lancou uma Pokebola em {self.wild_pokemon.nome}!")
        
        # Chance de captura baseada no HP atual (quanto menor o HP, maior a chance)
        vida_relativa = self.wild_pokemon.get_vida_atual() / self.wild_pokemon.hp_maximo
        chance_base = 0.3 # 30% de chance base
        chance_final = chance_base + (1.0 - vida_relativa) * 0.5 # Pode chegar a 80% se o HP estiver quase 0
        
        print("Balancando...")
        time.sleep(1)
        
        if random.random() < chance_final:
            print(f"GOTCHA! O {self.wild_pokemon.nome} foi capturado!")
            self.player.adicionar_pokemon(self.wild_pkm_clone if hasattr(self, 'wild_pkm_clone') else self.wild_pokemon)
            # Nota: O objeto wild_pokemon eh alterado na batalha, talvez devesse clonar antes se quiser ele full HP.
            # Mas por simplicidade, adicionamos o objeto atual.
            return True
        else:
            print(f"Ah nao! O {self.wild_pokemon.nome} escapou da Pokebola!")
            return False
