from models.estabelecimento import Estabelecimento

class Floresta(Estabelecimento):
    """
    Classe filha que representa a floresta.
    Permite batalhar com outros pokemons.
    """
    def __init__(self):
        super().__init__("Floresta", tempo_de_ir=2)