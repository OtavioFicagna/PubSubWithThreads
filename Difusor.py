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
def geraEnviaInformacao(gerador: Gerador):
    print(gerador.id)


# Main
def main():
    qtd_gerador = int(input("Digite a quantidade de geradores a serem criados: "))
    geradores = []

    #Estanciando os geradores
    for i in range(1, qtd_gerador+1):
        lista_informacao = list(map(int, input(f"Digite quais informações o gerador {i} vai gerar: ").split()))
        geradores.append(Gerador(i, lista_informacao))

if __name__ == "__main__":
    main()