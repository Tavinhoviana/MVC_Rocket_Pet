# exc_type: O tipo de excecao que ocorreu se houver
#     Se nao ocorreu nenhuma excecao, ente parametro sera None.

# exc_val: O tipo de excecao que ocorreu se houver
#     Se nao ocorreu nenhuma excecao, ente parametro sera None.

# exc_tb: O traceback (rastreamento de pilha) associado a excecao que ocorreu.
#     Se nao ocorreu nenhuma excecao, ente parametro sera None.

class AlgumaCoisa():
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saido")

with AlgumaCoisa() as something:
    print("Estou no meio")
