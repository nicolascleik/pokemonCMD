from models.pokemon import Pokemon
from . import arts

class Kyogre(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Kyogre",
            hp_maximo=450,
            poder_ataque=70,
            raridade="LENDARIO",
            arte_ascii=arts.kyogre
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Pulso de Origem (Origin Pulse) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
