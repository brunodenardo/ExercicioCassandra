from Servicos.AlteraProdutoLista import AlteraProdutoLista
from Servicos.SelectCompras import SelectCompras
from pprint import pprint

class MenuCompras:

    alterador = AlteraProdutoLista()
    selecionador = SelectCompras()

    def menu(self):
        key = 0

        while key != "V":
            print("\n--- Menu Compras ---\n")
            print("1 - Listar as compras de um usuário.")
            print("2 - Acionar um produto as compras.")

            key = input("\nEscolha uma ação (V para voltar para o menu principal): ")

            if key == "1":
                print("\nListar as compras de um usuário\n")
                pprint(self.selecionador.listarCompras()['usuario_compras'])
            elif key == "2":
                print("\nAcionar um produto as compras\n")
                self.alterador.adicionar("compras")
            elif key == "V":
                print("\nVoltando para o menu principal\n")
            else:
                print("\nAção invalida\n")