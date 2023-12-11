import json
from ConexaoCassandra import ConexaoCassandra
import uuid

class InsertUsuario:

    conexao = ConexaoCassandra()

    def insert(self):
        usuario = self.criaUsuario()
        usuario["id"] = uuid.uuid4()
        query = f'''
        INSERT INTO usuarios(
            id,
            usuario_email,
            usuario_endereco,
            usuario_login,
            usuario_nome,
            usuario_pagamento,
            usuario_senha, 
            usuario_telefone) 
        VALUES(
            {usuario["id"]},
            '{usuario['usuario_email']}',
            '{usuario['usuario_endereco']}',
            '{usuario['usuario_login']}',
            '{usuario['usuario_nome']}',
            '{usuario['usuario_pagamento']}',
            '{usuario['usuario_senha']}',
            '{usuario['usuario_telefone']}')
        '''
        self.conexao.usar().execute(query)
        self.criaTabelasAuxiliares(usuario)


    def criaUsuario(self):
        print("\nCriação de Usuário\n")
        usuario = {}
        usuario["usuario_nome"] = input("Digite o nome do usuário: ")
        usuario["usuario_login"] = input("Digite o login do usuario: ")
        usuario["usuario_senha"] = input("Digite a senha do usuário: ")
        usuario["usuario_email"] = input("Digite o email do usuário: ")
        usuario["usuario_telefone"] = input("Digite o telefone do usuário: ")
        usuario["usuario_endereco"] = []
        resp = "sim"
        while resp == "sim":
            print("\nEndereço\n")
            endereco = {}
            endereco['endereco_bairro'] = input("Digite bairro do endereço: ")
            endereco['endereco_cep'] = input("Digite o cep do endereço: ")
            endereco['endereco_estado'] = input("Digite o estado do endereço: ")
            endereco['endereco_informacao_adicional'] = input("Digite as indoremações adicionais: ")
            endereco['endereco_numero'] = input("Digite o número do endereço: ")
            endereco['endereco_rua_avenida'] = input("Digite a rua e avenida do endereço: ")
            endereco['endereco_tipo'] = input("Digite a rua e avenida do endereço: ")
            usuario["usuario_endereco"].append(endereco)
            resp = input("\nDeseja cadastrar mais um endereço (sim/não): ")
        resp = "sim"
        usuario["usuario_endereco"] = json.dumps(usuario["usuario_endereco"])
        usuario["usuario_pagamento"] =[]
        while resp =="sim":
            print("\nForma de Pagamento\n")
            pagamento = {}
            pagamento["pagamento_tipo"] = input("Digite o tipo de pagamento: ")
            pagamento["pagamento_cartao"] = input("Digite o número do cartão: ")
            usuario["usuario_pagamento"].append(pagamento)
            resp = input("Deseja cadastrar mais uma forma de pagamento (sim/não):  ")
        usuario["usuario_pagamento"] = json.dumps(usuario["usuario_pagamento"])
        return usuario
    
    def criaTabelasAuxiliares(self, usuario):
        self.conexao.usar().execute(f"INSERT INTO favoritos(id, usuario_favoritos) VALUES({usuario['id']}, '[]')")
        self.conexao.usar().execute(f"INSERT INTO compras(id, usuario_compras) VALUES({usuario['id']}, '[]')")
        self.conexao.usar().execute(f"INSERT INTO historico(id, usuario_historico) VALUES({usuario['id']}, '[]')")
        