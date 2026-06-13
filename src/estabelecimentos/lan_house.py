from models.estabelecimento import Estabelecimento

class Lan_house(Estabelecimento):
    """
    Classe filha que representa a Lan house.
    """
    def __init__(self):
        super().__init__("Lan house", tempo_de_ir=2)