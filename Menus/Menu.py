from Menus.MenuUsuario import MenuUsuario
from Menus.MenuFavoritos import MenuFavorito
from Menus.MenuProduto import MenuProduto
from Menus.MenuCompras import MenuCompras
from Menus.MenuHistorico import MenuHistorico

class Menu:

    menuUsuario = MenuUsuario()
    menuFavorito = MenuFavorito()
    menuProduto = MenuProduto()
    menuHistorico = MenuHistorico()
    menuCompras = MenuCompras()

    def menu(self):
        key = 0
        while key != "S":
            print("\nMenu Principal\n")
            print("1 - CRUD Usuário")
            print("2 - CRUD Compras")
            print("3 - CRUD Favoritos")
            print("4 - CRUD Histórico")
            print("5 - CRUD Produto")

            key = input("Escolha uma das ações (S para sair): ")

            if key == "1":
                self.menuUsuario.menu()
            elif key == "2":
                self.menuCompras.menu()
            elif key == "3":
                self.menuFavorito.menu()
            elif key == "4":
                self.menuHistorico.menu()
            elif key == "5":
                self.menuProduto.menu()
            elif key == "S":
                print("\nAté logo\n")
            else:
                print("\nAção invalida\n")

        
    