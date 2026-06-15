from models.pokemon import Pokemon
from . import arts

class Dialga(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Dialga",
            hp_maximo=450,
            poder_ataque=40,
            raridade="LENDARIO",
            arte_ascii=arts.dialga
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Rugido do Tempo (Roar of Time) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
