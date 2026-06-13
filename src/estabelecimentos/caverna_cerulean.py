from models.estabelecimento import Estabelecimento

class Caverna_cerulean(Estabelecimento):
    """
    Classe filha que representa a Caverna cerulean.
    Permite fazer uma exploração arriscada e encontrar pokemons lendários, entretanto é possível que desmaie.
    """
    def __init__(self):
        super().__init__("Caverna Cerulean", tempo_de_ir=3)