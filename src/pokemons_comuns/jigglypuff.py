from models.pokemon import Pokemon
from . import arts

class Jigglypuff(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Jigglypuff",
            hp_maximo=100,
            poder_ataque=10,
            raridade="COMUM",
            arte_ascii=arts.jigglypuff
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Voz Desarmoniosa (Disarming Voice) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
