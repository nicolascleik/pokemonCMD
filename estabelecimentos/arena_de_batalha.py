import random
from models.estabelecimento import Estabelecimento
from models.batalha import Batalha

# "Chefões" da Arena
from pokemons_comuns.charizard import Charizard
from pokemons_comuns.blastoise import Blastoise
from pokemons_comuns.snorlax import Snorlax
from pokemons_comuns.gengar import Gengar


class ArenaDeBatalha(Estabelecimento):
    """
    Classe filha que representa a arena de batalha.
    Permite lutar contra Pokémons de alto nível por prêmios em dinheiro.
    Respeita o contrato de Estabelecimento e a injeção da Batalha.
    """

    def __init__(self):
        super().__init__("Arena de Batalha", tempo_de_ir=4)

        # A Arena tem um pool próprio de oponentes fortes
        self.oponentes_arena = [Charizard, Blastoise, Snorlax, Gengar]

        # O prêmio em dinheiro por vencer uma luta na Arena
        self.premio_vitoria = 150.0

    def interagir(self, jogador, relogio) -> None:
        while True:
            print("\n" + "⚔️ " * 10)
            print("        ARENA DE BATALHA        ")
            print("⚔️ " * 10)
            print(f"Saldo Atual: ${jogador.dinheiro:.2f}")
            print(f"1 - Entrar no Torneio (Gasta 2h e 30 Energia | Prêmio: ${self.premio_vitoria:.2f})")
            print("0 - Voltar para a Cidade")

            escolha = input("\nO que deseja fazer? ")

            if escolha == "0":
                print("Saindo da Arena...")
                break

            elif escolha == "1":
                # 1. Validações Pré-Combate
                if relogio.hora_atual + 2 >= 24:
                    print("\n[Recepcionista] 'Os torneios de hoje já acabaram. Volte amanhã!'")
                    continue
                if jogador.energia_atual <= 30:
                    print("\n[Recepcionista] 'Você parece fraco demais para lutar. Vá comer algo!'")
                    continue
                if not jogador.obter_equipe():
                    print("\n[Recepcionista] 'Você precisa de pelo menos um Pokémon na equipe para se inscrever!'")
                    continue

                # 2. Consumo de Recursos do Torneio
                relogio.avancar_tempo(2)
                jogador.gastar_energia(30)

                # 3. Preparação do Oponente
                oponente_classe = random.choice(self.oponentes_arena)
                adversario = oponente_classe()

                print(
                    f"\n[Locutor] 'SENHORAS E SENHORES! O desafiante {jogador.nome} enfrentará um poderoso {adversario.nome}!'")

                # 4. Injeção de Dependência da Batalha (Com Fuga Bloqueada!)
                batalha = Batalha(jogador, adversario, fuga_bloqueada=True)
                resultado = batalha.iniciar()

                # 5. Resolução da Batalha
                if not resultado:
                    # Se retornar False, o jogador teve a equipe inteira desmaiada (Game Over diário)
                    return  # Quebra o menu da Arena e devolve pro main.py aplicar a punição

                # Se a batalha acabou e o adversário está sem vida, o jogador venceu
                if adversario.vida_atual <= 0:
                    print(f"\n[Locutor] 'INCRÍVEL! {jogador.nome} DESTRUIU O ADVERSÁRIO!'")
                    print(f"Você recebeu o prêmio de ${self.premio_vitoria:.2f}!")
                    jogador.modificar_dinheiro(self.premio_vitoria)
                else:
                    # Caso bizarro onde o jogador jogue uma pokébola na arena
                    print("\n[Juiz] 'A luta acabou de forma inusitada.'")
            else:
                print("Opção inválida!")