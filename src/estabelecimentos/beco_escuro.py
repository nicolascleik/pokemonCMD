from models.estabelecimento import Estabelecimento

class BecoEscuro(Estabelecimento):
    """
    Local onde o jogador pode negociar dívidas com o Agiota.
    """

    def __init__(self):
        super().__init__("Beco Escuro", tempo_de_ir=1)
        self._agiota = agiota

    def interagir(self, jogador, relogio) -> None:
        """
        Interação estendida: aceita a instância do agiota para operações financeiras.
        """
        while True:
            print("\n--- O AGIOTA ESTÁ TE ESPERANDO NAS SOMBRAS ---")
            print(f"Saldo: ${jogador.dinheiro:.2f} | Dívida Atual: ${jogador.divida:.2f}")
            print("1 - Pegar empréstimo")
            print("2 - Pagar dívida")
            print("0 - Sair")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                try:
                    valor = float(input("Quanto deseja pegar emprestado? "))
                    prazo = int(input("Em quantos dias pretende pagar? "))
                    if agiota.pegar_emprestimo(valor, prazo):
                        print(f"\n[!] Empréstimo de ${valor:.2f} aprovado!")
                    else:
                        print("\n[!] O Agiota negou o pedido (você já tem uma dívida ativa).")
                except ValueError:
                    print("Entrada inválida.")

            elif escolha == "2":
                try:
                    valor = float(input(f"Quanto deseja pagar? (Dívida: ${jogador.divida:.2f}): "))
                    if agiota.pagar_divida(valor):
                        print("\n[!] Pagamento efetuado com sucesso.")
                    else:
                        print("\n[!] Pagamento recusado (saldo insuficiente ou valor inválido).")
                except ValueError:
                    print("Entrada inválida.")

            elif escolha == "0":
                print("Saindo do Beco Escuro...")
                break
            else:
                print("Opção inválida.")