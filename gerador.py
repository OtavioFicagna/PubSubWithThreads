import _thread
import time
import random
from queue import Queue
from threading import Lock

from informacoes import Informacao

# Constantes
T_MIN = 1
T_MAX = 10
V_MIN = 1
V_MAX = 10

# Variável global para controlar quando parar as threads
stop_threads = False

# Classes
class Gerador:
    def __init__(self, id, lista_informacao):
        self.id = id
        self.lista_informacao = lista_informacao
        self.informacoes_geradas = Queue()
        self.lock = Lock()  # Cada gerador tem seu próprio Lock

# Funções

#  Função responsável por instanciar as threads geradoras de cada gerador e enviar as informações
def enviaInformacao(gerador: Gerador):
    global stop_threads

    for tipo in gerador.lista_informacao:
        # Criar thread para gerar informação apenas uma vez por tipo
        _thread.start_new_thread(threadGeradora, (gerador, tipo, T_MIN, T_MAX, V_MIN, V_MAX))

    while not stop_threads:
        with gerador.lock:
            while not gerador.informacoes_geradas.empty():
                msg = gerador.informacoes_geradas.get()
                print(f"Gerador {gerador.id}: Tipo {msg.tipo}, Valor {msg.valor}")
        time.sleep(1)  # Pequena pausa para evitar um loop muito rápido

# Função responsável por gerar as informações e inserir na fila do gerador
def threadGeradora(gerador: Gerador, tipo, T_MIN, T_MAX, V_MIN, V_MAX):
    global stop_threads
    while not stop_threads:
        informacao = Informacao(0, tipo, random.randint(V_MIN, V_MAX)) 
        with gerador.lock:
            gerador.informacoes_geradas.put(informacao)
        time.sleep(random.randint(T_MIN, T_MAX))  # Pausa simulando o tempo de geração

# Função responsável por instanciar os geradores
def instanciaGeradores(qtdGeradores: int):
    geradores = []
    for i in range(1, qtdGeradores + 1):
        lista_informacao = list(map(int, input(f"Digite quais informações o gerador {i} vai gerar (separadas por espaço): ").split()))
        gerador = Gerador(i, lista_informacao)
        geradores.append(gerador)

    for i in range(len(geradores)):
        _thread.start_new_thread(enviaInformacao, (geradores[i],))

def listen():
    global stop_threads
    input("Digite enter para encerrar o programa!")
    stop_threads = True  # Sinalizar que as threads devem parar

# Main
def main():
    qtdGeradores = int(input("Digite a quantidade de geradores a serem criados: "))
    # Instanciando os geradores
    instanciaGeradores(qtdGeradores)

    # Função que aguarda o usuário
    listen()
    
    # Pequena pausa para dar tempo das threads finalizarem corretamente
    time.sleep(2)
    print("Programa encerrado.")

if __name__ == "__main__":
    main()
