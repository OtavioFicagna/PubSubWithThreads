from informacoes import Informacao
from queue import Queue
import threading
from threading import Event
import socket
import pickle
import time
import os

SERVER = '127.0.0.1'
PORT = 8080
destino = (SERVER, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

stop_event = Event()
buffer = Queue()

def parar():
    if not stop_event.is_set():
        stop_event.set()
        try:
            tcp.shutdown(socket.SHUT_RDWR)
            tcp.close()
        except Exception as e:
            print(f"Erro ao fechar o socket: {e}")
        finally:
            print("Programa encerrado.")
            os._exit(0)

def interface():
    while not stop_event.is_set():
        while not buffer.empty():
            msg = buffer.get()
            print(f'Tipo: {msg.tipo}, Sequência: {msg.seq}, Valor: {msg.valor}')
        time.sleep(0.1)

def enviar_inscricoes(topicos):
    if stop_event.is_set():
        return
    try:
        inscricoes_msg = pickle.dumps(topicos)
        tcp.sendall(inscricoes_msg)
    except Exception as e:
        print(f"Erro ao enviar inscrições: {e}")

def recebe_informacao():
    while not stop_event.is_set():
        try:
            msg = tcp.recv(1024)
            buffer.put(pickle.loads(msg))
        except (EOFError, ConnectionResetError, socket.error):
            if not stop_event.is_set():
                print("Conexão com o servidor perdida!")
                parar()
            break

def main():
    try:
        tcp.connect(destino)
        while True:
            topicos = set(map(int, input("Digite os tópicos para se inscrever (separados por espaço): ").split()))
            erro = False
            if len(topicos) == 0:
                erro = True
                print("É obrigatória a inscrição em pelo menos um tópico!")
            else:
                for t in topicos:
                    if t < 1 or t > 6:
                        print(f"Tópico: {t} é inválido! Digite os tópicos novamente.")
                        erro = True
            if not erro:
                break
        enviar_inscricoes(topicos)

        threads = [
            threading.Thread(target=interface),
            threading.Thread(target=recebe_informacao)
        ]

        for thread in threads:
            thread.start()

        input("Digite enter para parar o programa!\n")
        parar()
    except ConnectionRefusedError:
        print("Conexão recusada. Verifique a disponibilidade do servidor!")

if __name__ == "__main__":
    main()