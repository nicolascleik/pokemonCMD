from models.player import Player
from models.relogio import Relogio
from models.gameManager import GameManager
from models.agiota import Agiota
from models.batalha import Batalha

from estabelecimentos.casa import Casa
from estabelecimentos.mercadinho import Mercadinho
from estabelecimentos.centro_pokemon import CentroPokemon
from estabelecimentos.floresta import Floresta
from estabelecimentos.caverna_cerulean import CavernaCerulean
from estabelecimentos.lago_de_pesca import LagoDePesca
from estabelecimentos.cassino import Cassino
from estabelecimentos.arena_de_batalha import ArenaDeBatalha
from estabelecimentos.beco_escuro import BecoEscuro

from pokemons_comuns.pikachu import Pikachu
from pokemons_comuns.charmander import Charmander
from pokemons_comuns.bulbasaur import Bulbasaur
from pokemons_comuns.squirtle import Squirtle

# Pokémons usados como cobradores do Agiota
from pokemons_comuns.gengar import Gengar
from pokemons_comuns.haunter import Haunter
from pokemons_comuns.meowth import Meowth

import random

def limpar_tela():
    print("\n" * 100)

def _disparar_cobradores(player, relogio, game_manager):
    """
    Spawna um encontro com os Pokémons do agiota quando cobrador_ativo está True.
    Chamado no topo de cada iteração do game loop.
    A batalha tem fuga_bloqueada=False — o jogador pode tentar fugir, mas com risco.
    Se perder, aplica penalidade de desmaio normalmente.
    """
    cobradores = [Gengar, Haunter, Meowth]
    cobrador_classe = random.choice(cobradores)
    cobrador = cobrador_classe()

    print("\n" + "!" * 50)
    print(" OS POKÉMONS DO AGIOTA TE ENCONTRARAM NA RUA!")
    print("!" * 50)
    print(f" Um {cobrador.nome} bloqueou seu caminho!")
    print(" Você pode lutar ou tentar fugir...")
    input("Pressione Enter para iniciar o confronto...")

    batalha = Batalha(player, cobrador, fuga_bloqueada=False)
    resultado = batalha.iniciar()

    if not resultado:
        # O jogador perdeu a batalha com o cobrador — aplica penalidade
        game_manager.aplicar_penalidade_desmaio(relogio)


def _processar_virada_de_dia(relogio, player, agiota, dia_anterior):
    """
    Centraliza todos os eventos que devem ocorrer quando um novo dia começa.
    Chamado sempre que relogio.dia_atual avançou em relação a dia_anterior.
    """
    if relogio.dia_atual > dia_anterior:
        # 1. Juros e prazo do agiota
        agiota.verificar_virada_de_dia()

        # 2. Gasto diário obrigatório com comida
        CUSTO_DIARIO_COMIDA = 20.0
        pagou = player.cobrar_gastos_diarios(CUSTO_DIARIO_COMIDA)
        if pagou:
            print(f"\n[Dia {relogio.dia_atual}] Gastos diários com comida descontados: -${CUSTO_DIARIO_COMIDA:.2f}")
        else:
            print(f"\n[!] Você não tem dinheiro para se alimentar hoje! (Custo: ${CUSTO_DIARIO_COMIDA:.2f})")
            print("    Sem comida, sua energia máxima está reduzida até você conseguir pagar.")
            # Penalidade por fome: reduz energia máxima no dia seguinte
            # (uma derrota hard depende do GameManager.verificar_derrota)


def main():
    limpar_tela()
    print("====================================================")
    print("           BEM-VINDO AO POKÉMON CMD (HARD MODE)     ")
    print("====================================================")
    print("      A sua persistência arquitetural será testada! ")
    print("====================================================\n")

    nome = input("Qual o seu nome, jovem treinador? ").strip()
    if not nome:
        nome = "Ash"

    # Inicialização das Entidades de Estado
    player = Player(nome)
    relogio = Relogio()
    game_manager = GameManager(player)
    agiota = Agiota(player)

    # Escolha do Pokémon Inicial
    print("\nEscolha seu Pokémon inicial para começar a aventura:")
    print("1 - Pikachu (Elétrico)")
    print("2 - Charmander (Fogo)")
    print("3 - Bulbasaur (Planta)")
    print("4 - Squirtle (Água)")

    while True:
        escolha = input("Digite o número (1-4): ").strip()
        if escolha == "1":
            player.adicionar_pokemon(Pikachu())
            break
        elif escolha == "2":
            player.adicionar_pokemon(Charmander())
            break
        elif escolha == "3":
            player.adicionar_pokemon(Bulbasaur())
            break
        elif escolha == "4":
            player.adicionar_pokemon(Squirtle())
            break
        else:
            print("Escolha inválida! Tente novamente.")

    # Capital de giro inicial
    player.modificar_dinheiro(50.0)

    # O MAPA DO JOGO
    locais = [
        Casa(),
        Mercadinho(),
        CentroPokemon(),
        Floresta(),
        CavernaCerulean(),
        LagoDePesca(),
        Cassino(),
        ArenaDeBatalha(),
        BecoEscuro(agiota)
    ]

    input("\nSua jornada começa agora! Pressione Enter para continuar...")

    # ==========================================
    # O LOOP PRINCIPAL DO MUNDO (GAME LOOP)
    # ==========================================
    while True:
        limpar_tela()

        # --- A. COBRADORES DO AGIOTA (roda antes de tudo) ---
        # Se o prazo da dívida estourou, o encontro é forçado a cada turno.
        if agiota.cobrador_ativo:
            _disparar_cobradores(player, relogio, game_manager)

        # --- B. VERIFICAÇÃO DE FIM DE JOGO ---
        # Separamos vitória de derrota para garantir que apenas uma mensagem apareça.
        if game_manager.verificar_vitoria():
            print("\nParabéns! Encerrando o jogo...")
            break
        if game_manager.verificar_derrota():
            print("\nGame Over. Encerrando o jogo...")
            break

        # --- C. HUD GLOBAL ---
        print("=" * 60)
        print(
            f" DIA: {relogio.dia_atual:<3} | HORA: {relogio.hora_atual:02d}:00h | ENERGIA: {player.energia_atual}/{player.energia_maxima}")
        print(f" TREINADOR: {player.nome}")
        print(f" SALDO: ${player.dinheiro:.2f} | DÍVIDA: ${player.divida:.2f}")

        equipe = player.obter_equipe()
        if equipe:
            pkm_ativo = equipe[0]
            print(f" POKÉMON ATIVO: {pkm_ativo.nome} (HP: {pkm_ativo.vida_atual}/{pkm_ativo.hp_maximo})")
        else:
            print(" POKÉMON ATIVO: Nenhum (Alerta Crítico)")

        if agiota.cobrador_ativo:
            print(" [ALERTA] OS COBRADORES DO AGIOTA ESTÃO TE CAÇANDO!")
        print("=" * 60)

        # --- D. MENU DE EXIBIÇÃO DO MAPA ---
        print("\nPara onde você deseja viajar?")
        for i, local in enumerate(locais, 1):
            print(f" {i:2d} - {local.nome:<20} | Custo: {local.tempo_de_ir}h | Energia: -{local.tempo_de_ir * 10}")
        print("  0 - Sair do Jogo")

        opcao = input("\nEscolha seu destino: ").strip()

        if opcao == "0":
            confirmar = input("Tem certeza que deseja desistir da sua jornada? (s/n): ").lower().strip()
            if confirmar == 's':
                print("\nObrigado por jogar Pokémon CMD!")
                break
            continue

        try:
            indice = int(opcao) - 1
            if 0 <= indice < len(locais):
                local_escolhido = locais[indice]

                # Guarda o estado temporal antes do deslocamento
                dia_anterior = relogio.dia_atual

                # --- E. RESOLUÇÃO DE MOVIMENTAÇÃO ---
                desmaiou = local_escolhido.ir(relogio, player)

                if desmaiou:
                    # Desmaio na estrada: penalidade e virada de dia forçada
                    game_manager.aplicar_penalidade_desmaio(relogio)
                else:
                    # --- F. POLIMORFISMO: o local assume o controle ---
                    local_escolhido.interagir(player, relogio)

                    equipe = player.obter_equipe()
                    if equipe and all(p.vida_atual <= 0 for p in equipe):
                        print("\n[!] TODOS OS SEUS POKÉMONS DESMAIARAM! Você entra em pânico e desmaia também!")
                        game_manager.aplicar_penalidade_desmaio(relogio)

                # --- G. GATILHO DE VIRADA DE DIA (cobre desmaio e sono voluntário) ---
                # Funciona para os dois fluxos acima, pois ambos podem virar o dia.
                _processar_virada_de_dia(relogio, player, agiota, dia_anterior)

                input("\nPressione Enter para continuar a exploração...")
            else:
                print("Opção inválida! Escolha um número que esteja listado no mapa.")
                input("Pressione Enter para tentar novamente...")

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
            input("Pressione Enter para continuar...")
        except Exception as e:
            print(f"Erro fatal de execução tratado pelo barramento principal: {e}")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()