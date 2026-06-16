from models.pokemon import Pokemon
from . import arts

class Meowth(Pokemon):
    """
    Classe que representa o Pokémon Meowth.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.meowth
        
        super().__init__(
            nome="Meowth", 
            hp_maximo=45, 
            poder_ataque=12, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Mordida (Bite) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)