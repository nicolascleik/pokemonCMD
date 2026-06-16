from models.pokemon import Pokemon
from . import arts

class Chikoritta(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Chikoritta",
            hp_maximo=80,
            poder_ataque=12,
            raridade="COMUM",
            arte_ascii=arts.chikoritta
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Folha Navalha (Razor Leaf) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
