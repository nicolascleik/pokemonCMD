import random
from models.estabelecimento import Estabelecimento
from models.batalha import Batalha

# Importando TODOS os pokemons comuns
from pokemons_comuns.pikachu import Pikachu
from pokemons_comuns.charmander import Charmander
from pokemons_comuns.bulbasaur import Bulbasaur
from pokemons_comuns.squirtle import Squirtle
from pokemons_comuns.eevee import Eevee
from pokemons_comuns.meowth import Meowth
from pokemons_comuns.venonat import Venonat
from pokemons_comuns.butterfree import Butterfree
from pokemons_comuns.gengar import Gengar
from pokemons_comuns.mew import Mew
from pokemons_comuns.mimikyu import Mimikyu
from pokemons_comuns.slowpoke import Slowpoke
from pokemons_comuns.snorlax import Snorlax
from pokemons_comuns.charizard import Charizard
from pokemons_comuns.blastoise import Blastoise
from pokemons_comuns.jigglypuff import Jigglypuff
from pokemons_comuns.haunter import Haunter
from pokemons_comuns.chikoritta import Chikoritta

# Importando Pokemons Lendarios
from pokemons_lendarios.mewtwo import Mewtwo
from pokemons_lendarios.articuno import Articuno
from pokemons_lendarios.dialga import Dialga
from pokemons_lendarios.kyogre import Kyogre
from pokemons_lendarios.lugia import Lugia
from pokemons_lendarios.mesprit import Mesprit
from pokemons_lendarios.rayquaza import Rayquaza

class Floresta(Estabelecimento):
    """
    Classe filha que representa a floresta.
    Povoada com a Pokedex completa do projeto.
    """
    def __init__(self):
        super().__init__("Floresta", tempo_de_ir=2)
        
        # Lista de Pokemons Comuns
        self.comuns = [
            Pikachu, Charmander, Bulbasaur, Squirtle, 
            Eevee, Meowth, Venonat, Butterfree,
            Gengar, Mew, Mimikyu, Slowpoke, Snorlax,
            Charizard, Blastoise, Jigglypuff, Haunter, Chikoritta
        ]
        
        # Lista de Pokemons Lendarios
        self.lendarios = [
            Mewtwo, Articuno, Dialga, Kyogre, 
            Lugia, Mesprit, Rayquaza
        ]

    def rodar_floresta(self, player):
        while True:
            print("\n" + "T " * 15)
            print("      FLORESTA VIRIDIAN      ")
            print("T " * 15)
            print("1 - Procurar Pokemon Selvagem")
            print("0 - Sair da Floresta")
            
            escolha = input("\nO que deseja fazer? ")

            if escolha == "1":
                print("\nVoce caminha silenciosamente pela grama alta...")
                
                if random.random() < 0.8:
                    if random.random() < 0.05:
                        pkm_classe = random.choice(self.lendarios)
                        print("\nO AR ESTA FICANDO PESADO... ALGO PODEROSO SE APROXIMA!")
                    else:
                        pkm_classe = random.choice(self.comuns)
                    
                    wild_pkm = pkm_classe()
                    
                    batalha = Batalha(player, wild_pkm)
                    venceu_ou_fugiu = batalha.iniciar()
                    
                    if not venceu_ou_fugiu:
                        print("\nVoce foi derrotado! Um Pokemon selvagem foi demais para voce.")
                        return 
                    
                    input("\nPressione Enter para continuar na floresta...")
                else:
                    print("Nada alem de vento e folhas secas por aqui.")
                    input("\nPressione Enter para continuar...")

            elif escolha == "0":
                print("Saindo da floresta...")
                break
            else:
                print("Opcao invalida!")
