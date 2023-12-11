from ConexaoCassandra import ConexaoCassandra
import json
from pprint import pprint
from Servicos.SelectUsuarios import SelectUsuarios
from Servicos.InputNumerico import InputNumerico

class SelectFavorito:

    conexao = ConexaoCassandra()
    selecionadorUsuario = SelectUsuarios()
    inputNumerico = InputNumerico()

    def listarFavoritos(self):
        id = self.selecionadorUsuario.selecionarIdUsuario("ver os Favoritos")
        favoritos = self.conexao.usar().execute(f"SELECT * FROM favoritos WHERE id = {id}")
        for row in favoritos:
            row = row._asdict()
            row["usuario_favoritos"] = json.loads(row["usuario_favoritos"])
            numero = 0
            for favorito in row["usuario_favoritos"]:
                favorito["numero"] = numero
                numero += 1
            return row

    def selecionarFavorito(self, acao):
        favoritos = self.listarFavoritos()
        pprint(favoritos)
        numero = self.inputNumerico.inputIntLista(f"Selecione o numero do produto favorito que pretende {acao}: ", len(favoritos))
        favoritos["numero"] = numero
        return favoritos