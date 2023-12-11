from Servicos.AlteraProdutoLista import AlteraProdutoLista
from Servicos.SelectHistorico import SelectHistorico
from pprint import pprint

class MenuHistorico:

    alterador = AlteraProdutoLista()
    selecionador = SelectHistorico()

    def menu(self):
        key = 0

        while key != "V":
            print("\n--- Menu Histórico ---\n")
            print("1 - Listar os histórico de um usuário.")
            print("2 - Acionar produto aos histórico.")

            key = input("\nEscolha uma ação (V para voltar para o menu principal): ")

            if key == "1":
                print("\nListar os histórico de um usuário\n")
                pprint(self.selecionador.listarHistorico()['usuario_historico'])
            elif key == "2":
                print("\nAcionar produto aos histórico\n")
                self.alterador.adicionar("historico")
            elif key == "V":
                print("\nVoltando para o menu principal\n")
            else:
                print("\nAção invalida\n")



