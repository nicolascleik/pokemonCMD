import sys
import os

# Adiciona a pasta src ao path para os imports funcionarem corretamente
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from models.player import Player
from models.relogio import Relogio
from estabelecimentos.casa import Casa  
from estabelecimentos.hospital import Hospital
from estabelecimentos.mercadinho import Mercadinho
from estabelecimentos.arena_de_batalha import Arena_de_batalha
from estabelecimentos.centro_pokemon import Centro_pokemon
from estabelecimentos.floresta import Floresta
from estabelecimentos.cassino import Cassino
from estabelecimentos.lan_house import Lan_house
from pokemons_comuns.pikachu import Pikachu
from pokemons_comuns.charmander import Charmander
from pokemons_comuns.bulbasaur import Bulbasaur
from pokemons_comuns.squirtle import Squirtle

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_tela()
    print("====================================================")
    print("           BEM-VINDO AO POKEMON CMD                ")
    print("====================================================")
    print("      Prepare-se para sua jornada Pokemon!         ")
    print("====================================================\n")
    
    nome = input("Qual o seu nome, jovem treinador? ")
    if not nome:
        nome = "Ash"
        
    player = Player(nome)
    relogio = Relogio()
    
    # Escolha do inicial
    print("\nEscolha seu Pokemon inicial para começar a aventura:")
    print("1 - Pikachu (Eletrico)")
    print("2 - Charmander (Fogo)")
    print("3 - Bulbasaur (Planta)")
    print("4 - Squirtle (Agua)")
    
    while True:
        escolha = input("Digite o numero (1-4): ")
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
            print("Escolha invalida! Tente novamente.")

    # Instancia os locais
    casa = Casa()
    hospital = Hospital()
    mercadinho = Mercadinho()
    arena = Arena_de_batalha()
    centro = Centro_pokemon()
    floresta = Floresta()
    cassino = Cassino()
    lan_house = Lan_house()
    
    locais = [casa, hospital, mercadinho, floresta, arena, centro, cassino, lan_house]

    player.alterar_dinheiro(50.0) # Comeca com um pouco de dinheiro para pocoes
    
    input("\nSua jornada comeca agora! Pressione Enter para continuar...")

    while True:
        limpar_tela()
        print("="*50)
        print(f" DIA: {relogio.dia_atual} | HORA: {relogio.get_hora_atual():02d}:00")
        print(f" TREINADOR: {player.nome}")
        print(f" SALDO: ${player.get_dinheiro():.2f} | DIVIDA: ${player.divida:.2f}")
        
        if player.equipe:
            pkm = player.equipe[0]
            print(f" POKEMON ATIVO: {pkm.nome} (HP: {pkm.get_vida_atual()}/{pkm.hp_maximo})")
        
        print("="*50)
        
        print("\nOnde voce deseja ir agora?")
        for i, local in enumerate(locais, 1):
            print(f"{i:2d} - {local.nome:<20} | Custo: {local.tempo_de_ir}h")
        print(" 0 - Sair do Jogo")
        
        opcao = input("\nEscolha uma opcao: ")
        
        if opcao == "0":
            confirmar = input("Tem certeza que deseja sair? (s/n): ").lower()
            if confirmar == 's':
                print("\nSalvando progresso... (Brincadeira, ainda nao temos save!)")
                print("Obrigado por jogar Pokemon CMD!")
                break
            continue
            
        try:
            indice = int(opcao) - 1
            if 0 <= indice < len(locais):
                local_escolhido = locais[indice]
                
                # Viaja para o local
                desmaiou = local_escolhido.ir(relogio)
                
                if desmaiou:
                    print("\n" + "!"*40)
                    print("EXAUSTAO! Voce passou da meia-noite e desmaiou!")
                    print("Um bom samaritano te encontrou e te levou ao Hospital.")
                    print("!"*40)
                    relogio.dormir(player)
                    input("\nPressione Enter para acordar no hospital...")
                    hospital.rodar_hospital(player)
                else:
                    # Logica de interacao baseada no local
                    if isinstance(local_escolhido, Casa):
                        while True:
                            limpar_tela()
                            print(f"\n--- {local_escolhido.nome} ---")
                            print("1 - Descansar na cama (Dormir ate o dia seguinte)")
                            print("0 - Voltar para a rua")
                            sub = input("\nO que deseja fazer? ")
                            if sub == "1":
                                local_escolhido.dormir(player, relogio)
                                input("\nPressione Enter para continuar...")
                                break
                            elif sub == "0":
                                break
                    
                    elif isinstance(local_escolhido, Hospital):
                        local_escolhido.rodar_hospital(player)
                        
                    elif isinstance(local_escolhido, Mercadinho):
                        local_escolhido.rodar_mercadinho(player)
                        
                    elif isinstance(local_escolhido, Cassino):
                        local_escolhido.rodar_cassino(player)
                    
                    elif isinstance(local_escolhido, Centro_pokemon):
                        print("\n--- CENTRO POKEMON ---")
                        print("Aqui voce podera gerenciar seu PC no futuro.")
                        player.get_equipe()
                        input("\nPressione Enter para voltar...")
                        
                    elif isinstance(local_escolhido, Floresta):
                        local_escolhido.rodar_floresta(player)

                    elif isinstance(local_escolhido, Arena_de_batalha):
                        print("\n--- ARENA DE BATALHA ---")
                        print("A arena esta fechada para reformas. Volte em breve!")
                        input("\nPressione Enter para voltar...")
                    
                    else:
                        print(f"\nVoce chegou ao {local_escolhido.nome}.")
                        print("Ainda nao ha atividades disponiveis aqui.")
                        input("\nPressione Enter para voltar...")
            else:
                print("Opcao invalida! Escolha um numero da lista.")
                input("Pressione Enter para tentar novamente...")
        except ValueError:
            print("Entrada invalida! Digite apenas numeros.")
            input("Pressione Enter para continuar...")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
