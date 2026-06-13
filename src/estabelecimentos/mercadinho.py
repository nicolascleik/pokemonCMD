from models.estabelecimento import Estabelecimento

class Mercadinho(Estabelecimento):
    """
    Classe filha que representa o mercadinho.
    Permite comprar pokebolas e poções.
    """
    def __init__(self):
        super().__init__("Mercadinho", tempo_de_ir=1)