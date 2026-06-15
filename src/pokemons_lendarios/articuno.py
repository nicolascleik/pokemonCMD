from models.pokemon import Pokemon
from . import arts

class Articuno(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Articuno",
            hp_maximo=400,
            poder_ataque=35,
            raridade="LENDARIO",
            arte_ascii=arts.articuno
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Raio de Gelo (Ice Beam) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
