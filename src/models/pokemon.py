from abc import ABC, abstractmethod


class Pokemon(ABC):
    """
    Superclasse abstrata que serve de molde para todos os Pokémon do jogo.
    Garante o encapsulamento dos atributos de combate e os limites de pontos de vida.
    """

    def __init__(self, nome: str, hp_maximo: int, poder_ataque: int, raridade: str, arte_ascii: str):
        self._nome: str = nome.strip().upper()
        self._hp_maximo: int = max(1, hp_maximo)
        self._poder_ataque: int = max(0, poder_ataque)
        self._raridade: str = raridade.strip().upper()
        self._arte_ascii: str = arte_ascii

        self._vida_atual: int = self._hp_maximo

    # --- PROPRIEDADES (Getters encapsulados com @property) ---

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def hp_maximo(self) -> int:
        return self._hp_maximo

    @property
    def poder_ataque(self) -> int:
        return self._poder_ataque

    @property
    def raridade(self) -> str:
        return self._raridade

    @property
    def arte_ascii(self) -> str:
        return self._arte_ascii

    @property
    def vida_atual(self) -> int:
        """Substitui o antigo get_vida_atual()."""
        return self._vida_atual

    # --- MECÂNICAS DE COMBATE E SAÚDE ---

    def receber_dano(self, dano: int) -> None:
        """Reduz a vida do Pokémon, garantindo o limite mínimo de zero."""
        if dano > 0:
            self._vida_atual -= dano
            if self._vida_atual < 0:
                self._vida_atual = 0
            print(f"{self._nome} recebeu {dano} de dano!")

    def curar(self, quantidade: int = None) -> None:
        """
        Restaura os pontos de vida do Pokémon.

        Se 'quantidade' for None, restaura totalmente (Centro Pokémon).
        Se 'quantidade' for informada, soma o valor à vida atual,
        mas utiliza a função min() para impedir que ultrapasse o hp_maximo.
        """
        if quantidade is None:
            # Cura total
            self._vida_atual = self._hp_maximo
            print(f"{self._nome} foi totalmente curado!")
        else:
            # Cura parcial: soma a vida atual com a cura, e corta no hp_maximo
            nova_vida = self._vida_atual + quantidade
            self._vida_atual = min(nova_vida, self._hp_maximo)
            print(f"{self._nome} recuperou {quantidade} de HP!")

    @abstractmethod
    def atacar(self, alvo) -> None:
        """
        Método abstrato. Obriga as classes filhas (Agua, Fogo, Eletrico)
        a implementarem suas próprias lógicas de ataque e multiplicadores de dano.
        """
        pass

    def __str__(self) -> str:
        return f"[{self._nome}] HP: {self._vida_atual}/{self._hp_maximo} | ATK: {self._poder_ataque} ({self._raridade})"