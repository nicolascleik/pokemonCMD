class Estabelecimento:
    """Classe base para todos os locais exploráveis do jogo."""
    def __init__(self, nome: str, tempo_de_ir: int):
        self.nome = nome.upper()
        self.tempo_de_ir = tempo_de_ir

    def ir(self, relogio) -> bool:
        """
        Calcula o tempo de viagem passando o objeto relógio atual do jogo.
        Retorna True se o jogador desmaiou de exaustão na viagem, False se chegou bem.
        """
        print(f"\nViajando para {self.nome}... (Custo: {self.tempo_de_ir}h)")
        
        desmaiou = relogio.avancar_tempo(self.tempo_de_ir)
        
        return desmaiou