import random


class Agiota:
    """
    Gerenciador do sistema de dívidas e cobranças.
    Isola a lógica financeira de risco do resto do jogo.
    """

    def __init__(self, jogador):
        self._jogador = jogador
        self._juros_diarios: float = 0.10  # 10% ao dia
        self._prazo_dias: int = 0
        self._dias_passados: int = 0
        self._cobrador_ativo: bool = False

    @property
    def cobrador_ativo(self) -> bool:
        """Flag que indica se o jogador está sendo caçado."""
        return self._cobrador_ativo

    def pegar_emprestimo(self, valor: float, prazo_dias: int) -> bool:
        """Inicia um empréstimo se o jogador não tiver dívidas ativas."""
        if self._jogador.divida > 0:
            print("O agiota ri da sua cara: 'Pague o que me deve primeiro!'")
            return False

        self._jogador.modificar_divida(valor)
        self._jogador.modificar_dinheiro(valor)
        self._prazo_dias = prazo_dias
        self._dias_passados = 0
        self._cobrador_ativo = False
        print(f"Empréstimo de ${valor:.2f} realizado. Prazo: {prazo_dias} dia(s).")
        return True

    def pagar_divida(self, valor: float) -> bool:
        """Tenta abater a dívida usando o saldo atual do jogador."""
        if self._jogador.dinheiro >= valor:
            self._jogador.modificar_dinheiro(-valor)
            self._jogador.modificar_divida(-valor)
            print(f"Você pagou ${valor:.2f} da sua dívida.")

            # Se quitou a dívida, limpa a ficha e cancela os cobradores
            if self._jogador.divida <= 0:
                print("Dívida totalmente quitada. O agiota te deixa em paz... por enquanto.")
                self._prazo_dias = 0
                self._dias_passados = 0
                self._cobrador_ativo = False
            return True

        print("Você não tem dinheiro suficiente para esse pagamento!")
        return False

    def verificar_virada_de_dia(self) -> None:
        """
        Aplica juros e verifica prazos.
        DEVE ser chamado pelo loop principal logo após relogio.virar_dia().
        """
        if self._jogador.divida > 0:
            # Aplica os juros
            juros = self._jogador.divida * self._juros_diarios
            self._jogador.modificar_divida(juros)
            self._dias_passados += 1

            print(f"[Agiota] Juros diários aplicados. Dívida atual: ${self._jogador.divida:.2f}")

            if self._dias_passados > self._prazo_dias:
                self._cobrador_ativo = True
                print("[ALERTA] O prazo estourou! Os Pokémons do Agiota estão atrás de você!")