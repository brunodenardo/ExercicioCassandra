import json
from pprint import pprint 
from ConexaoCassandra import ConexaoCassandra
from collections import namedtuple
from cassandra.util import OrderedMapSerializedKey
from Servicos.InputNumerico import InputNumerico

class SelectUsuarios:

    conexao = ConexaoCassandra()
    inputNumerico = InputNumerico()

    def listarTodos(self):
        resposta = self.conexao.usar().execute("select id, usuario_nome, usuario_email, usuario_telefone from usuarios;")
        listaResultado = []
        numero = 0
        for row in resposta:
            row = row._asdict()
            row["numero"] = numero
            numero += 1
            listaResultado.append(row)
        return listaResultado
    
    def selecionarIdUsuario(self, acao):
        lista = self.listarTodos()
        pprint(lista)
        numero = self.inputNumerico.inputIntLista(f"Selecione o numero do usúario que pretende {acao}: ", len(lista))
        id = lista[numero]["id"]
        return id
    
    def selecionar(self, acao):
        lista = self.listarTodos()
        pprint(lista)
        numero = self.inputNumerico.inputIntLista(f"Selecione o numero do usúario que pretende {acao}: ", len(lista))
        usuario = lista[numero]
        return usuario
            
    
    def listarDetalhesUsuario(self, id):
        resposta = self.conexao.usar().execute(f"select * from usuarios Where id = {id}")
        for row in resposta:
            row = row._asdict()
            row["usuario_endereco"] = json.loads(row["usuario_endereco"])
            row["usuario_pagamento"] = json.loads(row["usuario_pagamento"])
            return row