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
    Gerencia a compra de suprimentos, a venda de itens (como Peixes)
    e a oportunidade de trabalho no estoque.
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
            print(f"\nSeu Saldo: ${jogador.dinheiro:.2f}")
            print("======== MERCADINHO POKÉMON ========")
            print("1: Comprar Itens")
            print("2: Vender Itens (Peixes e Sobras)")
            print("3: Trabalhar no estoque (Gasta 4h e 40 de Energia | Ganha $60.00)")
            print("0: Sair da loja")
            print("====================================")

            opcao_principal = input("Escolha uma opção: ").strip()

            if opcao_principal == "0":
                print("Obrigado e volte sempre!")
                break

            # ==========================================
            # COMPRA DE ITENS
            # ==========================================
            elif opcao_principal == "1":
                while True:
                    print(f"\nSeu Saldo: ${jogador.dinheiro:.2f}")
                    print("--- MENU DE COMPRAS ---")
                    print(f"1: {p_pequena.nome} - ${p_pequena.valor:.2f}")
                    print(f"2: {p_grande.nome} - ${p_grande.valor:.2f}")
                    print(f"3: {p_bola.nome} - ${p_bola.valor:.2f}")
                    print(f"4: {salgado.nome} - ${salgado.valor:.2f}")
                    print(f"5: {marmita.nome} - ${marmita.valor:.2f}")
                    print(f"6: {maca.nome} - ${maca.valor:.2f}")
                    print("0: Voltar ao menu principal")
                    print("-----------------------")

                    escolha = input("Digite o número do item que deseja comprar (ou 0 para voltar): ").strip()

                    if escolha == "0":
                        break

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
                        jogador.modificar_dinheiro(-valor_total)
                        jogador.adicionar_item(item_escolhido.nome, quantidade)
                        print(f"Compra efetuada com sucesso! Você gastou ${valor_total:.2f}.")
                    else:
                        print(f"Saldo insuficiente. Faltam ${(valor_total - jogador.dinheiro):.2f}.")

            # ==========================================
            # VENDA DE ITENS (Mecânica Nova)
            # ==========================================
            elif opcao_principal == "2":
                while True:
                    print(f"\nSeu Saldo: ${jogador.dinheiro:.2f}")
                    print("--- MENU DE VENDAS (Preço de Recompra) ---")

                    # Tabela de itens aceitos para venda e seus respectivos valores
                    # Itens normais são recomprados a 50% do valor. Peixe tem valor fixo de $25.00.
                    itens_venda = [
                        ("PEIXE", 25.00),
                        (p_pequena.nome, p_pequena.valor * 0.5),
                        (p_grande.nome, p_grande.valor * 0.5),
                        (p_bola.nome, p_bola.valor * 0.5),
                        (salgado.nome, salgado.valor * 0.5),
                        (marmita.nome, marmita.valor * 0.5),
                        (maca.nome, maca.valor * 0.5)
                    ]

                    for idx, (nome_item, valor_venda) in enumerate(itens_venda, 1):
                        status = "[Possui]" if jogador.possui_item(nome_item.upper()) else "[Não possui]"
                        print(f"{idx}: {nome_item:<15} - Receba: ${valor_venda:.2f} {status}")
                    print("0: Voltar ao menu principal")
                    print("------------------------------------------")

                    escolha = input("Digite o número do item que deseja vender (ou 0 para voltar): ").strip()

                    if escolha == "0":
                        break

                    try:
                        idx_escolhido = int(escolha) - 1
                        if 0 <= idx_escolhido < len(itens_venda):
                            nome_item, valor_venda = itens_venda[idx_escolhido]
                            nome_item_upper = nome_item.upper()

                            # Validação inicial via interface pública do Player
                            if not jogador.possui_item(nome_item_upper):
                                print(f"\n[!] Você não possui {nome_item} no seu inventário para vender!")
                                continue

                            try:
                                qtd_venda = int(input(f"Quantas unidades de {nome_item} deseja vender? "))
                                if qtd_venda <= 0:
                                    print("Quantidade inválida.")
                                    continue
                            except ValueError:
                                print("Por favor, digite apenas números inteiros!")
                                continue

                            # Loop de consumo seguro para respeitar o dicionário privado do Player
                            qtd_realmente_vendida = 0
                            for _ in range(qtd_venda):
                                if jogador.possui_item(nome_item_upper):
                                    jogador.consumir_item(nome_item_upper)
                                    qtd_realmente_vendida += 1
                                else:
                                    break

                            if qtd_realmente_vendida > 0:
                                total_ganho = valor_venda * qtd_realmente_vendida
                                jogador.modificar_dinheiro(total_ganho)
                                print(
                                    f"\n[!] Sucesso! Você vendeu {qtd_realmente_vendida}x {nome_item} e recebeu ${total_ganho:.2f}.")
                                if qtd_realmente_vendida < qtd_venda:
                                    print(
                                        f"(Nota: Você pediu para vender {qtd_venda}, mas só tinha {qtd_realmente_vendida} em estoque).")
                            else:
                                print("\n[!] Erro crítico ao tentar processar a venda.")
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Opção inválida! Digite um número correspondente.")

            # ==========================================
            # TRABALHAR NO ESTOQUE
            # ==========================================
            elif opcao_principal == "3":
                tempo_turno = 4
                custo_energia = 40
                salario = 60.0

                if jogador.energia_atual <= custo_energia:
                    print(
                        "\n[Gerente] 'Você parece que vai desmaiar! Vá comer alguma coisa antes de tentar carregar caixas.'")
                    continue

                if relogio.hora_atual + tempo_turno >= 24:
                    print("\n[Gerente] 'Nosso turno acabou por hoje. Vá para casa e volte amanhã!'")
                    continue

                print("\nVocê veste o uniforme e passa horas carregando caixas de poções...")
                relogio.avancar_tempo(tempo_turno)
                jogador.gastar_energia(custo_energia)
                jogador.modificar_dinheiro(salario)

                print(f"Turno finalizado! Você recebeu ${salario:.2f}.")
                print(f"Agora são {relogio.hora_atual}:00h.")

            else:
                print("Opção inválida.")