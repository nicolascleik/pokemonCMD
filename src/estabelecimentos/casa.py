from models.estabelecimento import Estabelecimento

class Casa(Estabelecimento):
    """
    Classe filha que representa a residência do jogador.
    Permite descansar com segurança total e reiniciar o ciclo diário.
    """
    def __init__(self):
        super().__init__("Casa do Jogador", tempo_de_ir=3)

    def dormir(self, jogador, relogio):
        """
        Realiza a ação de dormir na própria cama.
        Zera o dia atual, avança para as 06:00 e dispara o cálculo de juros.
        """
        print("\n🏠 Você se deita em sua cama confortável e relaxa...")
        relogio.dormir(jogador)
        print("💤 Suas energias foram completamente restauradas!")