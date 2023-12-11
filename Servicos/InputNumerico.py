

class InputNumerico:

    def inputIntLista(self, texto, tamanhoLista):
        while True:
            resposta = input(texto)
            if resposta.isdigit():
                if int(resposta) <= tamanhoLista -1:
                    return int(resposta)
            print("\nResposta invalida\n")

    def inputFloat(self, texto):
        while True:
            resposta = input(texto)
            if self.is_numero(resposta):
                return float(resposta)
            print("\nResposta invalida\n")

    def inputInt(self, texto):
        while True:
            resposta = input(texto)
            if resposta.isdigit():
                return int(resposta)
            print("\nResposta invalida\n")
        

    def is_numero(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False