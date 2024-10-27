import _thread
import socket
import pickle

SERVER = '127.0.0.1'
PORT = 8080
destino = (SERVER, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect(destino)

inscricoes: set
conteudo_recebido: list

def inicializar():
    global inscricoes
    inscricoes = set(map(int, input("Insira os tópicos de inscrição separados por espaço: ").split()))

    enviar_inscricoes()

def parar():
    global tcp, inscricoes
    
    inscricoes = {}
    enviar_inscricoes()
    
    tcp.close()
    exit(0)

def esperar_usuario():
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

def exibir_informacoes():
    raise NotImplementedError()

def main():
    inicializar()

    esperar_usuario()

    exibir_informacoes()

if __name__ == "__main__":
    main()