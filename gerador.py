import threading
from threading import Lock, Event
import time
import random
import socket
import pickle
from queue import Queue

# Importando a classe informação
from informacoes import Informacao

# Parametros Servidor
SERVER_DIFUSOR = '127.0.0.1'
PORT_DIFUSOR = 5000

# Criando o socket de conexão com o difusor
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (SERVER_DIFUSOR, PORT_DIFUSOR)

# Constantes
T_MIN = 1
T_MAX = 10
V_MIN = 1
V_MAX = 10

# Variável global para controlar quando parar as threads
stop_event = Event()

# Classes
class Gerador:
    def __init__(self, id, lista_informacao):
        self.id = id
        self.lista_informacao = lista_informacao
        self.informacoes_geradas = Queue()
        self.lock = Lock()  # Cada gerador tem seu próprio Lock

# Funções

# Função responsável por instanciar as threads geradoras de cada gerador e enviar as informações
def enviaInformacao(gerador: Gerador):
    for tipo in gerador.lista_informacao:
        # Criar thread para gerar informação apenas uma vez por tipo
        threading.Thread(target=threadGeradora, args=(gerador, tipo, T_MIN, T_MAX, V_MIN, V_MAX)).start()

    while not stop_event.is_set():
        with gerador.lock:
            while not gerador.informacoes_geradas.empty():
                informacao = gerador.informacoes_geradas.get()
                try:
                    udp.sendto(pickle.dumps(informacao), dest)
                    #print(f"Gerador {gerador.id}: Tipo {informacao.tipo}, Valor {informacao.valor}")
                except socket.error as e:
                    print(f"Não foi possível enviar a mensagem! Erro: {e}")
        time.sleep(1)

# Função responsável por gerar as informações e inserir na fila do gerador
def threadGeradora(gerador: Gerador, tipo, T_MIN, T_MAX, V_MIN, V_MAX):
    while not stop_event.is_set():
        informacao = Informacao(0, tipo, random.randint(V_MIN, V_MAX)) 
        with gerador.lock:
            gerador.informacoes_geradas.put(informacao)
        time.sleep(random.randint(T_MIN, T_MAX))

# Função responsável por instanciar os geradores
def instanciaGeradores(qtdGeradores: int):
    geradores = []
    for i in range(1, qtdGeradores + 1):
        while True:
            try:
                lista_informacao = list(map(int, input(f"Digite quais informações o gerador {i} vai gerar (separadas por espaço): ").split()))
                if all(1 <= num <= 6 for num in lista_informacao):
                    gerador = Gerador(i, lista_informacao)
                    geradores.append(gerador)
                    break
                else:
                    print("Erro: Todos os números devem estar entre 1 e 6.")
            except ValueError:
                print("Erro: Por favor, digite apenas números inteiros separados por espaço.")

    for gerador in geradores:
        threading.Thread(target=enviaInformacao, args=(gerador,)).start()

def listen():
    input("Aperte enter para encerrar o programa!")
    stop_event.set()

# Main
def main():
    while True:
        try:
            qtdGeradores = int(input("Digite a quantidade de geradores a serem criados: "))
            break
        except ValueError:
            print("Erro: A quantidade de geradores deve ser um número inteiro!")
    # Instanciando os geradores
    instanciaGeradores(qtdGeradores)

    # Aguarda o usuário para encerrar
    listen()

    print("Encerrando programa...")

if __name__ == "__main__":
    main()