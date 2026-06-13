from models.pokemon import Pokemon
from . import arts

class Snorlax(Pokemon):
    """
    Classe que representa o Pokémon Snorlax.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.snorlax
        
        super().__init__(
            nome="Snorlax", 
            hp_maximo=50, 
            poder_ataque=10, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Cabeçada (Headbutt) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)