from models.pokemon import Pokemon
from . import arts

class Mesprit(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Mesprit",
            hp_maximo=350,
            poder_ataque=50,
            raridade="LENDARIO",
            arte_ascii=arts.mesprit
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Psiquico (Psychic) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
