from Servicos.SelectFavorito import SelectFavorito
from pprint import pprint
from Servicos.AlteraProdutoLista import AlteraProdutoLista
from Servicos.TirarFavorito import TirarFavorito

class MenuFavorito:

    selecionador = SelectFavorito()
    alterador = AlteraProdutoLista()
    removedor = TirarFavorito()

    def menu(self):
        key = 0

        while key != "V":
            print("\n--- Menu Favoritos ---\n")
            print("1 - Listar os favoritos de um usuário.")
            print("2 - Acionar produto aos favoritos.")
            print("3 - Remover produto dos favoritos.\n")

            key = input("\nEscolha uma ação (V para voltar para o menu principal): ")

            if key == "1":
                print("\nListar os favoritos de um usuário\n")
                pprint(self.selecionador.listarFavoritos()['usuario_favoritos'])
            elif key == "2":
                print("\nAcionar produto aos favoritos\n")
                self.alterador.adicionar("favoritos")
            elif key == "3":
                print("\nRemover produto dos favoritos\n")
                self.removedor.remover()
            elif key == "V":
                print("\nVoltando para o menu principal\n")
            else:
                print("\nAção invalida\n")


