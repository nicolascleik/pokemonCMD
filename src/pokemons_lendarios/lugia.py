from models.pokemon import Pokemon
from . import arts

class Lugia(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Lugia",
            hp_maximo=420,
            poder_ataque=55,
            raridade="LENDARIO",
            arte_ascii=arts.lugia
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Explosao Aeriana (Aeroblast) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
