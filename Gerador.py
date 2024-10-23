import _thread

# Classes
class Informacao:
    def __init__(self, seq, tipo, valor):
        self.seq = seq
        self.tipo = tipo
        self.valor  = valor

class Gerador:
    def __init__(self, id, lista_informacao):
        self.id = id
        self.lista_informacao = lista_informacao

# Funções

# Função responsavel por instanciar as threads geradoras de cada gerador e enviar as informações
def enviaInformacao(gerador: Gerador):
    print()

def threadGeradora():
    print()

# Main
def main():
    qtd_gerador = int(input("Digite a quantidade de geradores a serem criados: "))
    geradores = []

    #Estanciando os geradores
    for i in range(1, qtd_gerador+1):
        lista_informacao = list(map(int, input(f"Digite quais informações o gerador {i} vai gerar: ").split()))
        gerador = Gerador(i, lista_informacao)
        _thread.start_new_thread(enviaInformacao, (gerador,))

if __name__ == "__main__":
    main()