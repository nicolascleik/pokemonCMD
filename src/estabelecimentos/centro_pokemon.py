from models.estabelecimento import Estabelecimento

class Centro_pokemon(Estabelecimento):
    """
    Classe filha que representa o Centro pokemon.
    Permite ver e modificar sua equipe pokemon.
    """
    def __init__(self):
        super().__init__("Centro pokemon", tempo_de_ir=1)