from abc import ABC, abstractmethod

class Item(ABC):
    """
    Classe base estritamente abstrata.
    Garante que nenhum 'Item' genérico seja instanciado, apenas subclasses concretas.
    """

    def __init__(self, nome: str, valor: float):
        self._nome: str = nome.strip().upper()
        self._valor: float = max(0.0, valor)

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def valor(self) -> float:
        return self._valor

    @abstractmethod
    def usar(self, alvo) -> bool:
        """
        Contrato obrigatório: Toda classe filha DEVE implementar sua própria lógica.

        O 'alvo' é genérico (pode ser o Player, um Pokemon, etc).
        Deve obrigatoriamente retornar True se o item foi gasto, e False caso contrário.
        """
        pass

    def __str__(self) -> str:
        return f"{self._nome} | Preço: ${self._valor:.2f}"