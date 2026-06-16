from models.item import Item

class Marmita(Item):
    def __init__(self):
        super().__init__("MARMITA", 25.0)

    def usar(self, jogador) -> bool:
        if jogador.energia_atual >= jogador.energia_maxima:
            print("Você já está de barriga cheia!")
            return False

        jogador.recuperar_energia(40)  # Recupera 40 de fome
        return True