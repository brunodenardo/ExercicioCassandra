from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectProduto import SelectProduto

class DeleteProduto:

    conexao = ConexaoCassandra()
    selecionador = SelectProduto()

    def deletar(self):
        produto = self.selecionador.selecionarProduto("Deletar")
        query = f"DELETE FROM produtos WHERE id = {produto['id']}"
        self.conexao.usar().execute(query)

