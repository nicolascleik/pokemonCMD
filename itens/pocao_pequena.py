from models.item import Item

class PocaoPequena(Item): 
    def __init__(self):
        super().__init__("POÇÃO PEQUENA", 20.0) 
        self.poder_cura = 20

    def usar(self, alvo) -> bool:
        if alvo.vida_atual >= alvo.hp_maximo:
            print(f"{alvo.nome} já está com a vida cheia!")
            return False

        print(f"Usando {self.nome} em {alvo.nome}...")
        alvo.curar(self.poder_cura)
        return True