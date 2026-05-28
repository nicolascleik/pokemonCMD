import random

class Player:
    """
    Classe que representa o jogador e gerencia seus recursos (dinheiro, equipe e inventário).
    """
    def __init__(self, nome: str):
        self.nome: str = nome.upper()
        self.__dinheiro: float = 0.0
        self.divida: float = 0.0
        self.tamanho_bolsa_de_pokemons = 3
        self.equipe: list = []
        self.inventario: dict = {}

    def tentar_fugir(self):
        """
        Calcula a chance de fuga do jogador (50% de chance).
        Retorna True se conseguiu fugir, False se falhou.
        """
        print(f"{self.nome} está tentando fugir...")
        
        sucesso = random.choice([True, False]) 
        
        if sucesso:
            print("Você fugiu com sucesso!")
            return True
        else:
            print("Não foi possível fugir! O Pokémon selvagem bloqueou o caminho!")
            return False

    
    # --- GERENCIAMENTO FINANCEIRO ---
    def get_dinheiro(self):
        return self.__dinheiro

    def alterar_dinheiro(self, quantidade: float):
        """Adiciona ou remove dinheiro. Impede que o saldo fique negativo."""
        self.__dinheiro += quantidade
        if self.__dinheiro < 0:
            self.__dinheiro = 0.0

    def contrair_divida(self, valor: float):
        self.divida += valor

    def pagar_divida(self, valor: float):
        """Paga uma parte ou o total da dívida usando o dinheiro atual."""
        if self.__dinheiro >= valor:
            self.alterar_dinheiro(-valor)
            self.divida -= valor
            if self.divida < 0:
                self.divida = 0.0
            print(f"Dívida de ${valor} paga com sucesso!")
        else:
            print("Dinheiro insuficiente para pagar esse valor da dívida.")

    def aplicar_juros_diarios(self):
        """Aplica 10% de juros na dívida ao dormir."""
        if self.divida > 0:
            self.divida += (self.divida * 0.10)

    # --- GERENCIAMENTO DE INVENTÁRIO ---
    def adicionar_item(self, nome_item: str, quantidade: int = 1):
        """Adiciona um item ao dicionário do inventário."""
        if nome_item in self.inventario:
            self.inventario[nome_item] += quantidade
        else:
            self.inventario[nome_item] = quantidade
        print(f"{quantidade}x {nome_item}(s) adicionado(s) ao inventário!")

    def usar_item(self, nome_item: str):
        """Consome um item do inventário, removendo a chave se chegar a zero."""
        if nome_item in self.inventario:
            if self.inventario[nome_item] > 1:
                self.inventario[nome_item] -= 1
            else:
                self.inventario.pop(nome_item)
            return True
        else:
            print(f"Você não tem {nome_item} no inventário.")
            return False

    # --- GERENCIAMENTO DA EQUIPE ---
    def adicionar_pokemon(self, pokemon):
        """Adiciona um objeto Pokémon à lista (array) da equipe."""
        if len(self.equipe) < self.tamanho_bolsa_de_pokemons: # Limite de pokemons baseado na bolsa do jogador --- pode aumentar caso ele compre uma bolsa maior no mercadinho
            self.equipe.append(pokemon)
            print(f"{pokemon.nome} foi adicionado à sua equipe!")
        else:
            print(f"Sua equipe já está cheia! (Máximo de {self.tamanho_bolsa_de_pokemons}).")

    def get_equipe(self):
        """Lista todos os pokemons do jogador."""
        if not self.equipe:
            print("Sua equipe está vazia.")
        else:
            print(f"--- Equipe de {self.nome} ---")
            for pokemon in self.equipe:
                print(pokemon)

    def remover_pokemon(self, nome_pokemon: str):
        """Busca o pokemon pelo nome na equipe e o remove caso exista."""
        nome_pokemon = nome_pokemon.upper() 
        for pokemon in self.equipe:
            if pokemon.nome == nome_pokemon:
                self.equipe.remove(pokemon)
                print(f"{pokemon.nome} foi removido da sua equipe.")
                return True 
                
        print(f"{nome_pokemon} não foi encontrado na sua equipe.")
        return False

    def __str__(self):
        return f"JOGADOR: {self.nome} | Saldo: ${self.__dinheiro:.2f} | Dívida: ${self.divida:.2f}"