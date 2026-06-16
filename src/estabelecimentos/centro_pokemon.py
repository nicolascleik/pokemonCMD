from models.estabelecimento import Estabelecimento

class CentroPokemon(Estabelecimento):
    """
    Classe filha que representa o Centro Pokémon (Hospital).
    Permite visualizar a equipe, curar Pokémons específicos ou todos, mediante pagamento.
    Respeita o contrato de Estabelecimento e o encapsulamento do Player.
    """

    def __init__(self):
        super().__init__("Centro Pokémon", tempo_de_ir=1)
        self.custo_cura = 30.0

    def interagir(self, jogador, relogio) -> None:
        while True:
            equipe = jogador.obter_equipe()

            print("\n" + "=" * 40)
            print("   BEM-VINDO AO CENTRO POKÉMON!   ")
            print("=" * 40)
            print(f"Seu Saldo: ${jogador.dinheiro:.2f}")
            print(f"Taxa médica por Pokémon: ${self.custo_cura:.2f}\n")

            if not equipe:
                print("Você não tem Pokémons na equipe.")
                input("Pressione Enter para sair...")
                break

            print("--- Sua Equipe ---")
            for i, pkm in enumerate(equipe):
                print(f"{i + 1} - {pkm.nome} (HP: {pkm.vida_atual}/{pkm.hp_maximo})")

            print("\nOpções:")
            print("1 a X: Digite o número do Pokémon para curar")
            print("T: Curar toda a equipe de uma vez")
            print("0: Sair do Centro Pokémon")

            escolha = input("\nO que deseja fazer? ").strip().upper()

            if escolha == '0':
                print("\nEnfermeira Joy: Volte sempre que precisar!")
                break

            elif escolha == 'T':
                # Filtra apenas os Pokémons que realmente precisam de cura
                precisam_cura = [p for p in equipe if p.vida_atual < p.hp_maximo]

                if not precisam_cura:
                    print("\nSua equipe já está com a saúde perfeita!")
                    continue

                custo_total = len(precisam_cura) * self.custo_cura

                if jogador.dinheiro >= custo_total:
                    jogador.modificar_dinheiro(-custo_total)
                    for p in precisam_cura:
                        p.curar()  # Passando vazio, a cura é total
                    print(f"\nEquipe totalmente curada! Você pagou ${custo_total:.2f}.")
                else:
                    print(f"\nSaldo insuficiente! Você precisa de ${custo_total:.2f} para curar todos.")

            elif escolha.isdigit():
                idx = int(escolha) - 1

                if 0 <= idx < len(equipe):
                    pkm_escolhido = equipe[idx]

                    if pkm_escolhido.vida_atual == pkm_escolhido.hp_maximo:
                        print(f"\n{pkm_escolhido.nome} já está com a saúde cheia!")
                    elif jogador.dinheiro >= self.custo_cura:
                        jogador.modificar_dinheiro(-self.custo_cura)
                        pkm_escolhido.curar()
                        print(f"\n{pkm_escolhido.nome} foi curado com sucesso! Você pagou ${self.custo_cura:.2f}.")
                    else:
                        print("\nSaldo insuficiente para curar este Pokémon.")
                else:
                    print("\nNúmero de Pokémon inválido na sua equipe.")
            else:
                print("\nOpção inválida.")