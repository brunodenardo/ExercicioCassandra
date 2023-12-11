from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectUsuarios import SelectUsuarios
import uuid
from Servicos.InputNumerico import InputNumerico

class InsertProduto:

    conexao = ConexaoCassandra()
    selecionadorUsuario = SelectUsuarios()
    inputNumerico = InputNumerico()

    def insert(self):
        produto = self.criaProduto()
        query = f"""
            INSERT INTO produtos(
                id,
                id_vendedor, 
                produto_descricao, 
                produto_nome,
                produto_oferta, 
                produto_preco
            )
            VALUES(
                {produto['id']},
                {produto['id_vendedor']},
                '{produto['produto_descricao']}',
                '{produto['produto_nome']}',
                {produto['produto_oferta']},
                {produto['produto_preco']}
            )
        """
        self.conexao.usar().execute(query)


    def criaProduto(self):
        produto = {}
        produto["id"] = uuid.uuid4()
        produto["id_vendedor"] = self.selecionadorUsuario.selecionarIdUsuario("vender o Produto")
        produto["produto_nome"] = input("Digite o nome do produto: ")
        produto["produto_descricao"] = input("Digite a descricao do produto: ")
        produto["produto_preco"] = self.inputNumerico.inputFloat("Digite o preço: ")
        produto["produto_oferta"] = self.inputNumerico.inputInt("Digite a porcentagem de desconto (só número inteiro): ")
        return produto