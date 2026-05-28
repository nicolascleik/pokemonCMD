class Pokemon:
    """
    Superclasse abstrata que serve de molde para todos os Pokémon do jogo.
    """
    def __init__(self, nome: str, hp_maximo: int, poder_ataque: int, raridade: str ,arte_ascii: str):
        self.nome: str = nome.upper() 
        self.hp_maximo: int = hp_maximo
        self.raridade: str = raridade.upper()
        
        self.__vida_atual: int = hp_maximo 
        
        self.poder_ataque: int = poder_ataque
        self.arte_ascii: str = arte_ascii

    def get_vida_atual(self):
        return self.__vida_atual

    def receber_dano(self, dano: int):
        """Reduz a vida do Pokémon e garante que não fique menor que zero."""
        self.__vida_atual -= dano
        
        if self.__vida_atual < 0:
            self.__vida_atual = 0
            
        print(f"{self.nome} recebeu {dano} de dano!")

    def curar(self):
        """Restaura a vida do Pokémon ao máximo (usado no Centro Pokémon ou com Poção)"""
        self.__vida_atual = self.hp_maximo
        print(f"{self.nome} foi totalmente curado!")

    def atacar(self, alvo):
        """
        Método base de ataque. 
        Nas classes filhas (Agua, Fogo), esse método sofrerá Polimorfismo.
        """
        print(f"\n{self.arte_ascii}")
        print(f"{self.nome} ataca {alvo.nome} causando {self.poder_ataque} de dano!")
        alvo.receber_dano(self.poder_ataque)

    def __str__(self):
        return f"[{self.nome}] HP: {self.__vida_atual} | HP MAXIMO: {self.hp_maximo}"