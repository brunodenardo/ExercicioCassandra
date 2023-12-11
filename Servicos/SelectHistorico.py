from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectUsuarios import SelectUsuarios
import json

class SelectHistorico:

    conexao = ConexaoCassandra()
    selecionadorUsuario = SelectUsuarios()

    def listarHistorico(self):
        id = self.selecionadorUsuario.selecionarIdUsuario("ver o histórico")
        favoritos = self.conexao.usar().execute(f"SELECT * FROM historico WHERE id = {id}")
        for row in favoritos:
            row = row._asdict()
            row["usuario_historico"] = json.loads(row["usuario_historico"])
            numero = 0
            for favorito in row["usuario_historico"]:
                favorito["numero"] = numero
                numero += 1
            return row