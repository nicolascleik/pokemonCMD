from pokemon.pokemon import Pokemon
from . import arts

class Mewtwo(Pokemon):
    """
    Classe que representa o Pokémon lendário Mewtwo.
    É incrivelmente forte, mas não conta para o objetivo de Pokédex Comum.
    """
    def __init__(self):
        arte = arts.mewtwo
        
        super().__init__(
            nome="Mewtwo", 
            hp_maximo=500, 
            poder_ataque=45, 
            raridade="LENDARIO", 
            arte_ascii=arte
        )

    def atacar(self, alvo):
        print(f"\n{self.arte_ascii}")
        print(f"🔮 {self.nome} usou Confusão Mental (Psystrike) em {alvo.nome}!")
        print(f"A mente de {alvo.nome} sofreu um dano devastador de {self.poder_ataque}!")
        alvo.receber_dano(self.poder_ataque)