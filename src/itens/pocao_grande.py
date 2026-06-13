from models.item import Item

class PocaoGrande(Item): 
    def __init__(self):
        super().__init__("POÇÃO GRANDE", 50.0) 
        self.poder_cura = 50

    def usar(self, alvo): 
        print(f"Usando {self.nome} em {alvo.nome}...")
        
        alvo.receber_dano(-self.poder_cura)
        print(f"{alvo.nome} recuperou vida!")
        return True