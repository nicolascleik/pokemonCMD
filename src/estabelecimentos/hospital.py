from models.estabelecimento import Estabelecimento
from models.player import Player
from models.pokemon import Pokemon

class Hospital(Estabelecimento):
    """
    Classe filha que representa o hospital.
    Permite curar completamente sua equipe pokemon.
    """
    def __init__(self):
        super().__init__("Hospital", tempo_de_ir=2)

    def rodar_hospital(self, player):
        while True:
            print("\n==================================")
            print(" BEM-VINDO AO HOSPITAL POKEMON! ")
            print("==================================")
            print("Opção 1: Curar minha equipe")
            print("Opção 0: Sair")
            print("==================================\n")

            escolha = input('O que deseja fazer?\n')

            if escolha == '0':
                print('Até logo!')
                return

            elif escolha == '1':
                if not player.equipe:
                    print('Você não tem pokemons para curar.')
                    continue
                for pokemon in player.equipe:
                    pokemon.curar()

            else:
                print('Opção invalida, por favor selecione 0 ou 1!')