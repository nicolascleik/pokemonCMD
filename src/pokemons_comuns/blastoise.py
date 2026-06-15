from models.pokemon import Pokemon
from . import arts

class Blastoise(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Blastoise",
            hp_maximo=160,
            poder_ataque=22,
            raridade="COMUM",
            arte_ascii=arts.blastoise
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Hidro-Bomba (Hydro Pump) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
