class Item:
    """
    Classe base (Abstração) genérica para todos os itens do jogo.
    """
    def __init__(self, nome: str, valor: float):
        self.nome: str = nome.upper()
        self.valor: float = valor

    def usar(self, alvo):
        """
        Método base que será sobrescrito (Polimorfismo) pelas classes filhas.
        O 'alvo' pode ser um Pokemon (para curar/capturar).
        """
        pass

    def __str__(self):
        return f"{self.nome} | Preço: ${self.valor:.2f}"