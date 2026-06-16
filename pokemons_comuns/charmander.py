from models.pokemon import Pokemon
from . import arts

class Charmander(Pokemon):
    """
    Classe que representa o Pokémon Charmander.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.charmander
        
        super().__init__(
            nome="Charmander", 
            hp_maximo=40, 
            poder_ataque=15, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Investida (Tackle) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)