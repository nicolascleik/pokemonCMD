from models.estabelecimento import Estabelecimento

class Casa(Estabelecimento):
    """
    Classe filha que representa a residência do jogador.
    Cumpre o contrato de Estabelecimento e permite interações locais.
    """

    def __init__(self):
        super().__init__("Casa do Jogador", tempo_de_ir=1)

    def interagir(self, jogador, relogio) -> None:
        """
        O menu que aparece quando o jogador entra na casa.
        """
        while True:
            print(f"\n[{self.nome}] O que você deseja fazer?")
            print("1 - Dormir na cama (Avança para o próximo dia)")
            print("0 - Sair")

            escolha = input("Escolha: ")

            if escolha == "1":
                print("\n🏠 Você deita em sua cama confortável e relaxa...")

                # 1. Reseta o ciclo do tempo
                relogio.virar_dia()

                # 2. Restaura o estado biológico do jogador
                jogador.resetar_energia()
                print("💤 Suas energias foram completamente restauradas!")

                # (Opcional) Você pode adicionar uma pequena cura para os Pokémons ao dormir em casa
                for pkm in jogador.obter_equipe():
                    pkm.curar(20)

                # Obs: A cobrança do agiota será chamada pelo main.py quando perceber que o dia virou.

            elif escolha == "0":
                print("Você decidiu voltar para a cidade.")
                break
            else:
                print("Opção inválida.")