from Servicos.UpdateUsuario import UpdateUsuario
from Servicos.SelectUsuarios import SelectUsuarios
from Servicos.DeleteUsuario import DeleteUsuario
from Servicos.InsertUsuario import InsertUsuario
from pprint import pprint


class MenuUsuario:

    selecionador = SelectUsuarios()
    deletador = DeleteUsuario()
    atualizador = UpdateUsuario()
    insersor = InsertUsuario()


    def menu(self):
        key = 0
        while key != "V":
            print("\n--- Menu de Usuários ---\n")
            print("1 - Listar todos os Usuários.")
            print("2 - Ver detalher de um Usuários.")
            print("3 - Criar um Usuário.")
            print("4 - Deletar um Usuário.")
            print("5 - Atualizar um Usuário.\n")

            key = input("Escolha uma opção (V para voltar para o menu principal): ")

            if key == "1":
                print("\nListar Usuários\n")
                pprint(self.selecionador.listarTodos())
            elif key == "2":
                print("\nDetalhar Usuário\n")
                pprint(
                    self.selecionador.listarDetalhesUsuario(
                        self.selecionador.selecionarIdUsuario("Detalhar")
                    )
                )
            elif key == "3":
                print("\nCriar Usuário\n")
                self.insersor.insert()
            elif key == "4":
                print("\nDeletar Usuário\n")
                self.deletador.deletar()
            elif key == "5":
                print("\nAtualizar Usuário\n")
                self.atualizador.update()
            elif key == "V":
                print("\nVoltar para o menu principal\n")
            else:
                print("\nAção inexistente\n")