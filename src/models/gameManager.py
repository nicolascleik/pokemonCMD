import random

class GameManager:
    """
    Avalia as condições de vitória e derrota do jogo.
    Mantém o loop principal limpo.
    """

    def __init__(self, jogador):
        self._jogador = jogador

        # Condições de Vitória
        self._meta_lendarios: int = 5
        self._meta_dinheiro: float = 10000.0

    def verificar_derrota(self) -> bool:
        """
        Checa as condições de Game Over.
        Retorna True se o jogador perdeu o jogo.
        """
        # Falência total: Sem dinheiro, com dívida, sem como se curar
        if self._jogador.dinheiro <= 0 and self._jogador.divida > 0:
            if not self._jogador.possui_item("POKEBOLA") and not self._jogador.possui_item("POCAOGRANDE"):
                # Opcional: Você pode checar se a equipe toda está desmaiada aqui também
                print("\n" + "=" * 40)
                print("GAME OVER - FALÊNCIA ABSOLUTA")
                print("Você não tem dinheiro, itens ou como pagar o que deve.")
                print("=" * 40)
                return True

        # Fome: A morte por fome (não conseguir pagar comida) já retorna False
        # no cobrar_gastos_diarios do Player, então o main.py pode lidar com isso direto.
        return False

    def verificar_vitoria(self) -> bool:
        """
        Checa se o jogador cumpriu algum dos objetivos finais.
        Retorna True se venceu.
        """
        # Condição 1: Acúmulo de riqueza
        if self._jogador.dinheiro >= self._meta_dinheiro:
            print("\n" + "=" * 40)
            print("VITÓRIA CAPITALISTA!")
            print(f"Você acumulou ${self._meta_dinheiro:.2f} e comprou a sua própria liga Pokémon!")
            print("=" * 40)
            return True

        # Condição 2: Mestria Pokémon (Requer o método novo no Player)
        qtd_lendarios = self._jogador.contar_pokemons_por_raridade("LENDARIO")
        if qtd_lendarios >= self._meta_lendarios:
            print("\n" + "=" * 40)
            print("VITÓRIA DE MESTRE!")
            print(f"Você capturou {self._meta_lendarios} lendários e se tornou uma lenda viva!")
            print("=" * 40)
            return True

        return False

    def aplicar_penalidade_desmaio(self, relogio) -> None:
        """
        Calcula as perdas do jogador ao desmaiar de exaustão ou por estourar o horário.
        Reseta os status para o dia seguinte.
        """
        print("\n" + "!" * 40)
        print("VOCÊ DESMAIOU!")

        # Chance de 30% de ser roubado
        if random.random() <= 0.30:
            perda = self._jogador.dinheiro * 0.20  # Perde 20% do dinheiro
            self._jogador.modificar_dinheiro(-perda)
            print(f"Enquanto estava apagado na rua, alguém roubou ${perda:.2f} da sua carteira!")
        else:
            taxa_hospital = 50.0
            if self._jogador.dinheiro >= taxa_hospital:
                self._jogador.modificar_dinheiro(-taxa_hospital)
                print(f"A equipe de resgate te levou para casa. Taxa de emergência: ${taxa_hospital:.2f}")
            else:
                print("A equipe de resgate teve pena de você e te levou para casa de graça.")

        print("!" * 40)

        # O GameManager força o reset do ciclo
        relogio.virar_dia()
        self._jogador.resetar_energia()

        # Cura a equipe em 50% como benefício de ter dormido/sido resgatado
        for pkm in self._jogador.obter_equipe():
            pkm.curar(pkm.hp_maximo // 2)