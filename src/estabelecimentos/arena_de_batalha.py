from models.estabelecimento import Estabelecimento

class Arena_de_batalha(Estabelecimento):
    """
    Classe filha que representa a arena de batalha.
    Permite batalhar com outros pokemons.
    """
    def __init__(self):
        super().__init__("Arena de batalha", tempo_de_ir=4)