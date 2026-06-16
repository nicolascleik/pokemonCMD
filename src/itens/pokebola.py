from models.item import Item

class Pokebola(Item): 
    def __init__(self):
        super().__init__("POKEBOLA", 30.0)

    def usar(self, alvo) -> bool:
        # A Pokébola só pode ser usada de fato através do menu de Batalha
        print("Você não pode usar uma Pokébola assim! Entre em uma batalha primeiro.")
        return False