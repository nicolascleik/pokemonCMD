from models.estabelecimento import Estabelecimento
from itens.pocao_grande import PocaoGrande
from itens.pocao_pequena import PocaoPequena
from itens.pokebola import Pokebola
from itens.salgado import Salgado
from itens.marmita import Marmita
from itens.maca import Maca

class Mercadinho(Estabelecimento):
    """
    Classe filha que representa o mercadinho.
    Respeita o contrato de interagir e manipula apenas a interface pública do Player.
    """

    def __init__(self):
        super().__init__("Mercadinho", tempo_de_ir=1)

    def interagir(self, jogador, relogio) -> None:
        p_grande = PocaoGrande()
        p_pequena = PocaoPequena()
        p_bola = Pokebola()
        salgado = Salgado()
        marmita = Marmita()
        maca = Maca()

        while True:
            # Usando a propriedade encapsulada correta!
            print(f"\nSeu Saldo: ${jogador.dinheiro:.2f}")
            print("======== MERCADINHO POKÉMON ========")
            print(f"1: {p_pequena.nome} - ${p_pequena.valor:.2f}")
            print(f"2: {p_grande.nome} - ${p_grande.valor:.2f}")
            print(f"3: {p_bola.nome} - ${p_bola.valor:.2f}")
            print(f"4: {salgado.nome} - ${salgado.valor:.2f}")
            print(f"5: {marmita.nome} - ${marmita.valor:.2f}")
            print(f"6: {maca.nome} - ${maca.valor:.2f}")
            print("7: Trabalhar no estoque (Gasta 4h e 40 de Energia | Ganha $60.00)")
            print("0: Sair da loja")
            print("====================================")

            escolha = input("Digite o número do item que deseja (ou 0 para sair): ")

            if escolha == "0":
                print("Obrigado e volte sempre!")
                break  # Sai do loop do mercadinho e volta pro main

            item_escolhido = None
            if escolha == "1":
                item_escolhido = p_pequena
            elif escolha == "2":
                item_escolhido = p_grande
            elif escolha == "3":
                item_escolhido = p_bola
            elif escolha == "4":
                item_escolhido = salgado
            elif escolha == "5":
                item_escolhido = marmita
            elif escolha == "6":
                item_escolhido = maca
            elif escolha == "7":
                tempo_turno = 4
                custo_energia = 40
                salario = 60.0

                # 1. Validação de Energia
                if jogador.energia_atual <= custo_energia:
                    print(
                        "\n[Gerente] 'Você parece que vai desmaiar! Vá comer alguma coisa antes de tentar carregar caixas.'")
                    continue

                # 2. Validação de Tempo
                if relogio.hora_atual + tempo_turno >= 24:
                    print("\n[Gerente] 'Nosso turno acabou por hoje. Vá para casa e volte amanhã!'")
                    continue

                # 3. Aplicação da Mecânica
                print("\nVocê veste o uniforme e passa horas carregando caixas de poções...")
                relogio.avancar_tempo(tempo_turno)
                jogador.gastar_energia(custo_energia)
                jogador.modificar_dinheiro(salario)

                print(f"Turno finalizado! Você recebeu ${salario:.2f}.")
                # Como o relógio avançou, mostramos a nova hora ao jogador
                print(f"Agora são {relogio.hora_atual}:00h.")
            else:
                print("Opção inválida.")
                continue

            try:
                quantidade = int(input(f"Quantas unidades de {item_escolhido.nome} você quer? "))
                if quantidade <= 0:
                    print("Quantidade inválida.")
                    continue
            except ValueError:
                print("Por favor, digite apenas números inteiros!")
                continue

            valor_total = item_escolhido.valor * quantidade

            if jogador.dinheiro >= valor_total:
                # Remove o dinheiro usando valor negativo
                jogador.modificar_dinheiro(-valor_total)
                # Adiciona no inventário de forma normalizada
                jogador.adicionar_item(item_escolhido.nome, quantidade)
                print(f"Compra efetuada com sucesso! Você gastou ${valor_total:.2f}.")
            else:
                print(f"Saldo insuficiente. Faltam ${(valor_total - jogador.dinheiro):.2f}.")