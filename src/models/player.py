import random


class Player:
    """
    Classe que representa o jogador e centraliza a gestão de estado dos seus recursos.
    Siga o princípio do encapsulamento: nenhuma classe externa deve manipular
    as coleções ou saldos diretamente.
    """

    def __init__(self, nome: str):
        self.nome: str = nome.upper()
        self._dinheiro: float = 0.0
        self._divida: float = 0.0
        self._energia_maxima: int = 100
        self._energia_atual: int = self._energia_maxima
        self._tamanho_bolsa_de_pokemons: int = 3
        self._equipe: list = []
        self._inventario: dict[str, int] = {}

    # --- SERRALHERIA DE INVENTÁRIO ---

    def _normalizar_nome_item(self, nome_item: str) -> str:
        """Método utilitário interno para garantir consistência de chaves."""
        return nome_item.strip().upper()

    def possui_item(self, nome_item: str) -> bool:
        """
        Consulta segura de inventário.
        A Batalha deve chamar este método em vez de acessar o dict.
        """
        nome_tratado = self._normalizar_nome_item(nome_item)
        # O método .get() retorna 0 se a chave não existir, evitando KeyError
        return self._inventario.get(nome_tratado, 0) > 0

    def adicionar_item(self, nome_item: str, quantidade: int = 1) -> None:
        """Adiciona uma quantidade do item ao inventário de forma padronizada."""
        nome_tratado = self._normalizar_nome_item(nome_item)

        if nome_tratado in self._inventario:
            self._inventario[nome_tratado] += quantidade
        else:
            self._inventario[nome_tratado] = quantidade

        print(f"{quantidade}x {nome_tratado}(s) adicionado(s) ao inventário!")

    def consumir_item(self, nome_item: str) -> bool:
        """
        Consome um item se disponível.
        Retorna True se a operação foi bem-sucedida, False caso contrário.
        """
        nome_tratado = self._normalizar_nome_item(nome_item)

        if self.possui_item(nome_item):
            self._inventario[nome_tratado] -= 1

            # Limpeza de chaves vazias para não poluir a memória
            if self._inventario[nome_tratado] <= 0:
                del self._inventario[nome_tratado]

            return True

        print(f"Você não tem {nome_tratado} no inventário.")
        return False

    def expandir_bolsa(self, nova_capacidade: int) -> None:
        """Permite que o Mercadinho aumente o limite da equipe."""
        if nova_capacidade > self._tamanho_bolsa_de_pokemons:
            self._tamanho_bolsa_de_pokemons = nova_capacidade
            print(f"Capacidade da bolsa expandida para {nova_capacidade} Pokémons!")

    def contar_pokemons_por_raridade(self, raridade: str) -> int:
        """Utilizado pelo GameManager para checar a condição de vitória."""
        raridade_tratada = raridade.strip().upper()
        contador = sum(1 for pkm in self._equipe if pkm.raridade == raridade_tratada)
        return contador

    # --- FINANÇAS E SISTEMA DE FOME ---

    @property
    def dinheiro(self) -> float:
        return self._dinheiro

    @property
    def divida(self) -> float:
        return self._divida

    @property
    def capacidade_bolsa(self) -> int:
        return self._tamanho_bolsa_de_pokemons

    @property
    def energia_atual(self) -> int:
        return self._energia_atual

    @property
    def energia_maxima(self) -> int:
        return self._energia_maxima

    def gastar_energia(self, quantidade: int) -> bool:
        """
        Deduz energia ao viajar ou realizar trabalhos braçais.
        Retorna True se o jogador desmaiou de fome/exaustão (energia <= 0).
        """
        self._energia_atual -= quantidade
        if self._energia_atual <= 0:
            self._energia_atual = 0
            print(f"\n[!] A barriga de {self.nome} roncou alto... A visão escureceu de tanta fome e exaustão!")
            return True
        return False

    def recuperar_energia(self, quantidade: int) -> None:
        """Chamado quando o jogador consome um item de comida."""
        nova_energia = self._energia_atual + quantidade
        self._energia_atual = min(nova_energia, self._energia_maxima)
        print(f"Você comeu algo! Energia recuperada: {self._energia_atual}/{self._energia_maxima}")

    def resetar_energia(self) -> None:
        """Chamado pelo relógio quando o dia vira (dormir na cama)."""
        self._energia_atual = self._energia_maxima

    def modificar_dinheiro(self, quantidade: float) -> None:
        """Adiciona ou subtrai dinheiro, garantindo que o saldo não fique negativo."""
        self._dinheiro += quantidade
        if self._dinheiro < 0:
            self._dinheiro = 0.0

    def cobrar_gastos_diarios(self, custo_comida: float) -> bool:
        """
        Deduz o custo de sobrevivência diária.
        Retorna True se o jogador conseguiu pagar,
        ou False se não tiver dinheiro suficiente (Gatilho de Falência/Morte por Fome).
        """
        if self._dinheiro >= custo_comida:
            self.modificar_dinheiro(-custo_comida)
            return True
        return False

    def modificar_divida(self, quantidade: float) -> None:
        """
        Altera o valor total da dívida.
        A taxa de juros deve ser calculada externamente e injetada aqui.
        """
        self._divida += quantidade
        if self._divida < 0:
            self._divida = 0.0

    # --- GERENCIAMENTO DA EQUIPE (CONTRATO E POLIMORFISMO) ---

    def obter_equipe(self) -> list:
        """Retorna uma cópia da lista ou uma visão de leitura para evitar mutação externa."""
        return self._equipe.copy()

    def adicionar_pokemon(self, pokemon) -> bool:
        """
        Tenta adicionar um Pokémon à equipe respeitando o limite atual da bolsa.
        Retorna True se adicionado, False se a equipe estiver cheia.
        """
        if len(self._equipe) < self._tamanho_bolsa_de_pokemons:
            self._equipe.append(pokemon)
            print(f"{pokemon.nome} foi adicionado à sua equipe!")
            return True

        print(f"Sua equipe já está cheia! (Máximo de {self._tamanho_bolsa_de_pokemons}).")
        return False

    def remover_pokemon(self, nome_pokemon: str) -> bool:
        """Busca e remove o Pokémon pelo nome. Retorna True se removido."""
        nome_tratado = nome_pokemon.strip().upper()

        for i, pokemon in enumerate(self._equipe):
            if pokemon.nome == nome_tratado:
                removido = self._equipe.pop(i)
                print(f"{removido.nome} foi liberado da sua equipe.")
                return True

        print(f"{nome_tratado} não foi encontrado na sua equipe.")
        return False

    def tentar_fugir(self) -> bool:
        """Calcula a chance probabilística de fuga (50%)."""
        print(f"{self.nome} está tentando fugir...")
        return random.choice([True, False])

    def __str__(self) -> str:
        return f"JOGADOR: {self.nome} | Saldo: ${self._dinheiro:.2f} | Dívida: ${self._divida:.2f}"