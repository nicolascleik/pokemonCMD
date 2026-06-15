from models.pokemon import Pokemon
from . import arts

class Haunter(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Haunter",
            hp_maximo=90,
            poder_ataque=18,
            raridade="COMUM",
            arte_ascii=arts.haunter
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Sombra Noturna (Night Shade) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
