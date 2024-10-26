import _thread
import socket
import pickle

SERVER = '127.0.0.1'
PORT = 8080
destino = (SERVER, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect(destino)

inscricoes: set

def inicializar():
    global inscricoes
    inscricoes = list(map(int, input("Insira os tópicos de inscrição: ").split()))

    inscricoes_msg = pickle.dumps(inscricoes)

    tcp.sendto(inscricoes_msg, destino)

def esperar_usuario():
    while True:
        op = input("Operação")

        if op.lower() not in ['sub', 'unsub', 'kill']:
            print('OPERAÇÃO INVÁLIDA')
        
        else:
            raise NotImplementedError()


def exibir_informacoes():
    raise NotImplementedError()

def main():
    inicializar()

    esperar_usuario()

    exibir_informacoes()

if __name__ == "__main__":
    main()