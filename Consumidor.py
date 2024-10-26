import _thread
import socket

SERVER = '127.0.0.1'
PORT = 8080
destino = (SERVER, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect(destino)

inscricoes: set

def inicializar():
    global inscricoes
    inscricoes = list(map(int, input("Insira os tópicos de inscrição: ").split()))

def esperar_usuario():
    raise NotImplementedError()

def exibir_informacoes():
    raise NotImplementedError()

def main():
    inicializar()

    esperar_usuario()

    exibir_informacoes()

if __name__ == "__main__":
    main()