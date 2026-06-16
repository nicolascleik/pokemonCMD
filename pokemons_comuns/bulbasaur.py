from models.pokemon import Pokemon
from . import arts

class Bulbasaur(Pokemon):
    """
    Classe que representa o Pokémon Bulbasaur.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.bulbasaur
        
        super().__init__(
            nome="Bulbasaur", 
            hp_maximo=50, 
            poder_ataque=10, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Investida (Tackle) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)