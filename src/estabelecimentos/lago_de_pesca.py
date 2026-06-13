from models.estabelecimento import Estabelecimento

class Lago_de_pesca(Estabelecimento):
    """
    Classe filha que representa o lado de pesca.
    Permite pescar para achar pokemons tipo água.
    """
    def __init__(self):
        super().__init__("Lago de pesca", tempo_de_ir=2)