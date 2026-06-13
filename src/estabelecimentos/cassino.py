from models.estabelecimento import Estabelecimento

class Cassino(Estabelecimento):
    """
    Classe filha que representa o cassino.
    Permite utilizar da sorte e dinheiro para conseguir itens.
    """
    def __init__(self):
        super().__init__("Cassino", tempo_de_ir=2)