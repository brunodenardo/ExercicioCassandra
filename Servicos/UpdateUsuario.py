from ConexaoCassandra import ConexaoCassandra
from Servicos.SelectUsuarios import SelectUsuarios
import json

class UpdateUsuario:
    conexao = ConexaoCassandra()
    selecionador = SelectUsuarios()


    def update(self):
        usuarioAtualizado = self.geraNovosValores()
        query = f"""
        UPDATE usuarios
        SET
            usuario_email = '{usuarioAtualizado["usuario_email"]}',
            usuario_endereco = '{usuarioAtualizado["usuario_endereco"]}',
            usuario_login = '{usuarioAtualizado["usuario_login"]}',
            usuario_nome = '{usuarioAtualizado["usuario_nome"]}',
            usuario_pagamento = '{usuarioAtualizado["usuario_pagamento"]}',
            usuario_senha = '{usuarioAtualizado["usuario_senha"]}',
            usuario_telefone = '{usuarioAtualizado["usuario_telefone"]}'
        WHERE id = {usuarioAtualizado["id"]};
        """
        self.conexao.usar().execute(query)

    def geraNovosValores(self):
        id = self.selecionador.selecionarIdUsuario("Atualizar")
        usuario = self.selecionador.listarDetalhesUsuario(id)
        for chave, valor in usuario.items():
            if chave != "id":
                decisao = input(f"Deseja atualizar {chave} de valor {valor} (sim/nao): ")
                if chave != "usuario_endereco" and chave != "usuario_pagamento" and decisao == "sim":
                    novoValor = input(f"Digite o novo valor de {chave}: ")
                    usuario[chave] = novoValor
                elif decisao == "sim":
                    for indice, objeto in enumerate(usuario[chave]):
                        for chaveEndereco, valorEndereco in objeto.items():
                            decisaoEndereco = input(f"Deseja atualizar {chaveEndereco} de valor {valorEndereco} (sim/nao): ")
                            if decisaoEndereco == "sim":
                                novoValor = input(f"Digite o novo valor de {chaveEndereco}: ")
                                usuario[chave][indice][chaveEndereco] = novoValor
        usuario["usuario_endereco"] = json.dumps(usuario["usuario_endereco"])
        usuario["usuario_pagamento"] = json.dumps(usuario["usuario_pagamento"])
        return usuario
           
