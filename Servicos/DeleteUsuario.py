from pprint import pprint
from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectUsuarios import SelectUsuarios

class DeleteUsuario:

    conexao = ConexaoCassandra()
    selecionador = SelectUsuarios()

    def deletar(self):
        id = self.selecionador.selecionarIdUsuario("deletar")
        query = f"DELETE FROM usuarios WHERE id = {id}"
        self.conexao.usar().execute(query)
        self.deletarAuxiliares(id)

    def deletarAuxiliares(self, id):
        self.conexao.usar().execute(f"DELETE FROM favoritos WHERE id = {id}")
        self.conexao.usar().execute(f"DELETE FROM compras WHERE id = {id}")
        self.conexao.usar().execute(f"DELETE FROM historico WHERE id = {id}")





