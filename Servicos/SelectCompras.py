from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectUsuarios import SelectUsuarios
import json

class SelectCompras:

    conexao = ConexaoCassandra()
    selecionadorUsuario = SelectUsuarios()

    def listarCompras(self):
        id = self.selecionadorUsuario.selecionarIdUsuario("ver as compras")
        favoritos = self.conexao.usar().execute(f"SELECT * FROM compras WHERE id = {id}")
        for row in favoritos:
            row = row._asdict()
            row["usuario_compras"] = json.loads(row["usuario_compras"])
            numero = 0
            for favorito in row["usuario_compras"]:
                favorito["numero"] = numero
                numero += 1
            return row