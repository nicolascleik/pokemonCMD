from models.estabelecimento import Estabelecimento
from itens.pocao_grande import PocaoGrande
from itens.pocao_pequena import PocaoPequena
from itens.pokebola import Pokebola
from models.player import Player

class Mercadinho(Estabelecimento):
    """
    Classe filha que representa o mercadinho.
    Permite comprar pokebolas e poções.
    """
    def __init__(self):
        super().__init__("Mercadinho", tempo_de_ir=1)

    def rodar_mercadinho(self, player):
        p_grande = PocaoGrande()
        p_pequena = PocaoPequena()
        p_bola = Pokebola()
        
        while True:
            print(f"\nSeu Saldo: ${player._Player__dinheiro:.2f}")
            print("======== MERCADINHO POKÉMON ========")
            print(f"Opção 1: {p_pequena.nome} - Custa ${p_pequena.valor:.2f}")
            print(f"Opção 2: {p_grande.nome} - Custa ${p_grande.valor:.2f}")
            print(f"Opção 3: {p_bola.nome} - Custa ${p_bola.valor:.2f}")
            print("Opção 0: Sair da loja")
            print("====================================")

            escolha = input("Digite o número do item que deseja:\n")

            item_escolhido = None

            if escolha == "1":
                item_escolhido = p_pequena
            elif escolha == "2":
                item_escolhido = p_grande
            elif escolha == "3":
                item_escolhido = p_bola
            elif escolha == "0":
                print("Até mais!")
                return
            else:
                print("Por favor escolha um número entre 1 a 3.")
                continue
            
            
            quantidade = int(input(f'Quantas unidades de {item_escolhido.nome} você quer?\n'))
            if quantidade <= 0:
                print('Por favor insira uma quantidade maior que 0.')
                continue
            valor_total = item_escolhido.valor * quantidade

            if player.get_dinheiro() >= valor_total:
                player.alterar_dinheiro(-valor_total)
                player.adicionar_item(item_escolhido.nome, quantidade)
            else:
                print(f"Você não tem dinheiro suficiente para comprar {quantidade} {item_escolhido.nome}.")
