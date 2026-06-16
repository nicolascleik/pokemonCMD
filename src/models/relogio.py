class Relogio:
    """
    Classe responsável estritamente pelo controle do tempo cronológico do jogo.
    Siga o SRP: o relógio apenas conta horas e dias. Ele não deve conhecer
    regras de finanças, inventário ou biologia do jogador.
    """

    def __init__(self):
        self._hora_atual: int = 6
        self._dia_atual: int = 1
        self._LIMITE_MEIA_NOITE: int = 24

    # --- PROPRIEDADES (Getters encapsulados) ---

    @property
    def hora_atual(self) -> int:
        return self._hora_atual

    @property
    def dia_atual(self) -> int:
        return self._dia_atual

    # --- GESTÃO DO TEMPO ---

    def avancar_tempo(self, quantidade_horas: int) -> bool:
        """
        Avança o contador de horas.

        Retorna True se o jogador atingiu ou estourou o limite de 24h
        (Gatilho para o main.py saber que o jogador desmaiou na rua).
        """
        if quantidade_horas > 0:
            self._hora_atual += quantidade_horas

        # Checa se ultrapassou o limite e retorna explicitamente
        if self._hora_atual >= self._LIMITE_MEIA_NOITE:
            return True

        return False

    def virar_dia(self) -> None:
        """
        Reseta o relógio para as 06:00 AM do próximo dia.

        Deve ser chamado pelo fluxo principal do jogo em duas situações:
        1. Quando o jogador vai dormir voluntariamente na Casa.
        2. Quando o método avancar_tempo retornar True (desmaio por exaustão).
        """
        self._dia_atual += 1
        self._hora_atual = 6
        print(f"\n--- Amanheceu! Dia {self._dia_atual} - 06:00 AM ---")