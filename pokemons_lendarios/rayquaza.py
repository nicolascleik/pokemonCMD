from models.pokemon import Pokemon
from . import arts

class Rayquaza(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Rayquaza",
            hp_maximo=480,
            poder_ataque=65,
            raridade="LENDARIO",
            arte_ascii=arts.rayquaza
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Ascensao do Dragao (Dragon Ascent) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
