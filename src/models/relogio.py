class Relogio:
    def __init__(self):
        self.hora_atual = 6
        self.dia_atual = 1

    def avancar_tempo(self, quantidade_horas: int):
        """Avança as horas. Retorna True se atingiu ou passou da Meia-Noite[cite: 17, 54]."""
        if quantidade_horas > 0:
            self.hora_atual += quantidade_horas
        
        if self.hora_atual >= 24:
            return True
        return False

    def dormir(self, jogador):
        """Avança o relógio para as 06:00 do próximo dia e calcula os juros[cite: 36, 54]."""
        self.dia_atual += 1
        self.hora_atual = 6
        jogador.aplicar_juros_diarios()
        print(f"Amanheceu! Dia {self.dia_atual} - 06:00 AM.")

    def get_hora_atual(self):
        return self.hora_atual