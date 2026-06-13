from models.pokemon import Pokemon
from . import arts

class Pikachu(Pokemon):
    """
    Classe que representa o Pokémon Pikachu.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.pikachu
        
        super().__init__(
            nome="Pikachu", 
            hp_maximo=40, 
            poder_ataque=15, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Ataque rápido (Quick attack) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)