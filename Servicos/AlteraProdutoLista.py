from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectProduto import SelectProduto
from Servicos.SelectUsuarios import SelectUsuarios
import json
from pprint import pprint
from uuid import UUID

class AlteraProdutoLista:

    conexao = ConexaoCassandra()
    selecionadorProduto = SelectProduto()
    selecionadorUsuario = SelectUsuarios()

    def adicionar(self, tabela):
        usuario = self.selecionadorUsuario.selecionar(f"alterar {tabela}")
        produto = self.selecionadorProduto.selecionarProduto(f"adicionar em {tabela} de {usuario['usuario_nome']}")
        objeto = self.conexao.usar().execute(f"SELECT * FROM {tabela} WHERE id = {usuario['id']}")
        produto = {
            "produto_id":produto["id"],
            "produto_nome":produto["produto_nome"],
            "produto_oferta":produto["produto_oferta"],
            "produto_preco":produto["produto_preco"]
        }
        for obj in objeto:
            obj = obj._asdict()
            obj[f"usuario_{tabela}"] = json.loads(obj[f"usuario_{tabela}"])
            obj[f"usuario_{tabela}"].append(produto)
            obj[f"usuario_{tabela}"] = self.obj_serializer(obj[f"usuario_{tabela}"])
            obj[f"usuario_{tabela}"] = json.dumps(obj[f"usuario_{tabela}"])
            self.conexao.usar().execute(
                f"""UPDATE {tabela}
                SET usuario_{tabela} = '{obj[f'usuario_{tabela}']}'
                WHERE id = {obj['id']};""")
            

    def obj_serializer(self, lista):
        for obj in lista:
            obj["produto_id"] = str(obj["produto_id"])
            obj["produto_preco"] = str(obj["produto_preco"])
        return lista
    
