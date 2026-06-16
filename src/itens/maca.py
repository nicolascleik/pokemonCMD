from models.item import Item

class Maca(Item):
    def __init__(self):
        super().__init__("MAÇA", 5.0)

    def usar(self, jogador) -> bool:
        if jogador.energia_atual >= jogador.energia_maxima:
            print("Você já está de barriga cheia!")
            return False

        jogador.recuperar_energia(10)  # Recupera 10 de fome
        return True