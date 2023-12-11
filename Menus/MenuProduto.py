from pprint import pprint
from Servicos.DeleteProduto import DeleteProduto
from Servicos.UpdateProduto import UpdateProduto
from Servicos.SelectProduto import SelectProduto
from Servicos.InsertProduto import InsertProduto

class MenuProduto:

    insersor = InsertProduto()
    selecionador = SelectProduto()
    deletador = DeleteProduto()
    atualizador = UpdateProduto()


    def menu(self):
        key = 0
        while key != "V":
            print("\n--- Menu de Usuários ---\n")
            print("1 - Listar Produtos.")
            print("2 - Criar um Produto.")
            print("3 - Deletar um Produto.")
            print("4 - Atualizar um Produto.\n")

            key = input("Escolha uma opção (V para voltar para o menu principal): ")

            if key == "1":
                print("\nListar Produtos\n")
                pprint(self.selecionador.listarTodosProduto())
            elif key == "2":
                print("\nCriar Produto\n")
                self.insersor.insert()
            elif key == "3":
                print("\nDeletar Produto\n")
                self.deletador.deletar()
            elif key == "4":
                print("\nAtualizar Produto\n")
                self.atualizador.update()
            elif key == "V":
                print("\nVoltar para o menu principal\n")
            else:
                print("\nAção invalida\n")