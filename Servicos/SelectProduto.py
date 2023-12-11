from ConexaoCassandra import ConexaoCassandra
from pprint import pprint
from Servicos.InputNumerico import InputNumerico

class SelectProduto:

    conexao = ConexaoCassandra()
    inputNumerico = InputNumerico()

    def listarTodosProduto(self):
        resposta = self.conexao.usar().execute("SELECT * FROM produtos")
        lista = []
        numero = 0
        for produto in resposta:
            produto = produto._asdict()
            produto["numero"] = numero
            numero += 1
            lista.append(produto)
        return lista
    
    def selecionarProduto(self, acao):
        lista = self.listarTodosProduto()
        pprint(lista)
        numero = self.inputNumerico.inputIntLista(f"Selecione o numero do produto que pretende {acao}: ", len(lista))
        produto = lista[numero]
        return produto

