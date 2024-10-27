from informacoes import Informacao
from queue import Queue
import threading
import socket
import pickle

SERVER = '127.0.0.1'
PORT = 8080
destino = (SERVER, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect(destino)

inscricoes: set
conteudo_recebido: Queue

def parar():
    global tcp, inscricoes
    
    inscricoes = {}
    enviar_inscricoes()
    
    tcp.close()
    exit(0)

def tratar_input():
    global inscricoes
    while True:
        op = input("Operação").lower()

        if op not in ['sub', 'unsub', 'kill']:
            print('OPERAÇÃO INVÁLIDA')

        else:    
            if op == 'sub':
                novas_inscricoes = set(map(int, input('Insira os novos tópicos de inscrição: ').split()))
                inscricoes = inscricoes.union(novas_inscricoes)
                enviar_inscricoes()
          
            elif op == 'unsub':
                remocao = set(map(int, input('Insira os tópicos para se desinscrever: ').split()))
                inscricoes = inscricoes.difference(remocao)
                enviar_inscricoes()

            elif op == 'kill':
                parar()

def enviar_inscricoes():
    global inscricoes
    inscricoes_msg = pickle.dumps(inscricoes)

    tcp.sendall(inscricoes_msg)

def obter_informacoes():
    obj = tcp.recv(1024)
    conteudo_recebido.put(pickle.loads(obj))

def atualizar_gui():
    info: Informacao = conteudo_recebido.get()
    print(f'Informação é do tipo: {info.tipo}, sequência: {info.seq} e valor: {info.valor}')

def main():
    global inscricoes
    inscricoes = set(map(int, input("Insira os tópicos de inscrição separados por espaço: ").split()))
    enviar_inscricoes()

    input_handler = threading.Thread(target=tratar_input)
    input_handler.start()

    connection_handler = threading.Thread(target=obter_informacoes)
    connection_handler.start()
    
    interface = threading.Thread(target=atualizar_gui)
    interface.start()

if __name__ == "__main__":
    main()