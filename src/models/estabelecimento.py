from abc import ABC, abstractmethod


class Estabelecimento(ABC):
    """
    Classe base estritamente abstrata para todos os locais exploráveis do jogo.
    Define o contrato obrigatório de navegação e interação com o ecossistema.
    """

    def __init__(self, nome: str, tempo_de_ir: int):
        self._nome: str = nome.strip().upper()
        self._tempo_de_ir: int = max(0, tempo_de_ir)

    # --- PROPRIEDADES (Getters encapsulados) ---

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def tempo_de_ir(self) -> int:
        return self._tempo_de_ir

    # --- FLUXO DE NAVEGAÇÃO E POLIMORFISMO ---

    def ir(self, relogio, jogador) -> bool:
        """
        Orquestra o deslocamento do jogador até ao local.

        Retorna True se o jogador desmaiou de exaustão na viagem (passou da meia-noite),
        ou False se chegou em segurança.
        """
        custo_energia = self._tempo_de_ir * 10

        print(f"\nViajando para {self._nome}... (Custo: {self._tempo_de_ir}h | Energia: -{custo_energia})")

        # Consome os recursos
        desmaiou_tempo = relogio.avancar_tempo(self._tempo_de_ir)
        desmaiou_fome = jogador.gastar_energia(custo_energia)

        # Se qualquer um dos dois gatilhos for verdadeiro, ele desmaia
        return desmaiou_tempo or desmaiou_fome

    @abstractmethod
    def interagir(self, jogador, relogio) -> None:
        """
        Método abstrato que toda classe filha (Casa, Mercadinho, Cassino, etc.) 
        DEVE obrigatoriamente implementar.

        Aqui será colocado o sub-loop de menus ou lógicas específicas de cada local,
        recebendo as instâncias de jogador e relógio para manipular os estados.
        """
        pass