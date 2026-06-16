from models.pokemon import Pokemon
from . import arts

class Charizard(Pokemon):
    def __init__(self):
        super().__init__(
            nome="Charizard",
            hp_maximo=150,
            poder_ataque=25,
            raridade="COMUM", # No seu projeto, ele esta como comum apesar de ser forte
            arte_ascii=arts.charizard
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} usou Lanca-Chamas (Flamethrower) em {alvo.nome}!")
        alvo.receber_dano(self.poder_ataque)
