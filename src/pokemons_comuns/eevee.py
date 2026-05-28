from pokemon.pokemon import Pokemon
from . import arts

class Eevee(Pokemon):
    """
    Classe que representa o Pokémon Eevee.
    É um Pokémon do tipo Normal, de raridade Comum.
    """
    def __init__(self):
        arte = arts.eevee
        
        super().__init__(
            nome="Eevee", 
            hp_maximo=45, 
            poder_ataque=12, 
            raridade="COMUM", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"💫 {self.nome} usou Investida (Tackle) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)