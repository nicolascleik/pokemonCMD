from models.item import Item

class Salgadinho(Item):
    def __init__(self):
        super().__init__("SALGADINHO", 15.0)

    def usar(self, jogador) -> bool:
        if jogador.energia_atual >= jogador.energia_maxima:
            print("Você já está de barriga cheia!")
            return False

        jogador.recuperar_energia(20)  # Recupera 40 de fome
        return True