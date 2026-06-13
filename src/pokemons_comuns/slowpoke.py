from models.pokemon import Pokemon
from . import arts

class Slowpoke(Pokemon):
    """
    Classe que representa o Pokémon Slowpoke.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.slowpoke
        
        super().__init__(
            nome="Slowpoke", 
            hp_maximo=50, 
            poder_ataque=10, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Investida (Tackle) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)