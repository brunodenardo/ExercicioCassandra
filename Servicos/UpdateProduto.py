from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectProduto import SelectProduto
from Servicos.InputNumerico import InputNumerico

class UpdateProduto:

    conexao = ConexaoCassandra()
    selecionador = SelectProduto()
    inputNumerico = InputNumerico()
    #id | id_vendedor | produto_comentarios | produto_descricao | produto_nome | produto_numero_vendas | produto_oferta | produto_preco
    
    def update(self):
        novoProduto = self.criaProdutoAtualizado()
        query = f"""
            UPDATE produtos
            SET
                produto_descricao = '{novoProduto['produto_descricao']}',
                produto_nome = '{novoProduto['produto_nome']}',
                produto_oferta = {novoProduto['produto_oferta']},
                produto_preco = {novoProduto['produto_preco']}
            WHERE
                id = {novoProduto['id']};
        """
        self.conexao.usar().execute(query)


    def criaProdutoAtualizado(self):
        produto = self.selecionador.selecionarProduto("Atualizar")
        for chave, valor in produto.items():
            if chave != "id" and chave != "id_vendedor" and chave != "numero":
                decisao = input(f"Deseja atualizar {chave} de valor {valor} (sim/nao): ")
                if decisao == "sim":
                    if chave == "produto_preco":
                        novoValor = self.inputNumerico.inputFloat(f"Digite o novo valor de {chave}: ")
                        produto[chave] = novoValor
                    elif chave == "produto_oferta":
                        novoValor = self.inputNumerico.inputInt(f"Digite o novo valor de {chave}: ")
                        produto[chave] = novoValor
                    else:
                        novoValor = input(f"Digite o novo valor de {chave}: ")
                        produto[chave] = novoValor
        return produto
