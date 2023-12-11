from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectFavorito import SelectFavorito
import json
from Servicos.AlteraProdutoLista import AlteraProdutoLista

class TirarFavorito:

    conexao = ConexaoCassandra()
    selecionadorFavortitos = SelectFavorito()
    alteradorLista = AlteraProdutoLista()

    def remover(self):
        favoritos = self.selecionadorFavortitos.selecionarFavorito("remover")
        favoritos["usuario_favoritos"].pop(favoritos["numero"])
        favoritos["usuario_favoritos"] = self.alteradorLista.obj_serializer(favoritos["usuario_favoritos"])
        favoritos["usuario_favoritos"] = json.dumps(favoritos["usuario_favoritos"])
        self.conexao.usar().execute(f"""
            UPDATE favoritos
            SET usuario_favoritos = '{favoritos['usuario_favoritos']}'
            WHERE id = {favoritos['id']};""")

