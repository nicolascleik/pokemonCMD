from models.estabelecimento import Estabelecimento

class Hospital(Estabelecimento):
    """
    Classe filha que representa o hospital.
    Permite curar completamente sua equipe pokemon.
    """
    def __init__(self):
        super().__init__("Hospital", tempo_de_ir=2)