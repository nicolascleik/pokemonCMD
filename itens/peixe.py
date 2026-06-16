from models.item import Item

class Peixe(Item):
    def __init__(self):
        super().__init__("PEIXE", 40.0)

    def usar(self, alvo) -> bool:
        print("Você não pode comer um peixe cru! Venda-o no mercadinho.")
        return False