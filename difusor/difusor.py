from informacoes import Informacao
from queue import Queue, Empty
import threading
from threading import Event
import socket
import pickle
import time

HOST = '127.0.0.1'
PORT_GERADORES = 5000
PORT_CONSUMIDORES = 5010

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT_GERADORES))

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT_CONSUMIDORES))
tcp_socket.listen()

buffer_conteudo = Queue()
clientes_inscritos = {}
stop_event = Event()

print(f'Difusor escutando os geradores na porta {PORT_GERADORES}')
print(f'Difusor escutando os consumidores na porta {PORT_CONSUMIDORES}')

def lidar_com_inscricoes(socket_cliente):
    while not stop_event.is_set():
        try:
            data = socket_cliente.recv(1024)
            if not data:
                break
            topicos = pickle.loads(data)
            
            if 0 in topicos:
                clientes_inscritos[socket_cliente] = topicos
            else:
                if socket_cliente in clientes_inscritos:
                    del clientes_inscritos[socket_cliente]
                socket_cliente.close()
        except (OSError, pickle.PickleError):
            socket_cliente.close()
            break

def monitorar_clientes(server_socket):
    server_socket.settimeout(1)
    while not stop_event.is_set():
        try:
            client_socket, client_address = server_socket.accept()
            clientes_inscritos[client_socket] = set()
            client_thread = threading.Thread(target=lidar_com_inscricoes, args=(client_socket,))
            client_thread.daemon = True
            client_thread.start()
        except socket.timeout:
            continue
        except OSError:
            break
        
def enviar_para_clientes():
    while not stop_event.is_set():
        try:
            info = buffer_conteudo.get(timeout=1)
            for client_socket, topicos in list(clientes_inscritos.items()):
                if info.tipo in topicos:
                    try:
                        client_socket.send(pickle.dumps(info))
                        time.sleep(0.1)
                    except OSError:
                        del clientes_inscritos[client_socket]
        except Empty:
            continue

def monitorar_geradores():
    udp_socket.settimeout(1)
    seq = 0
    while not stop_event.is_set():
        try:
            msg, _endereco = udp_socket.recvfrom(1024)
            info = pickle.loads(msg)
            info.seq = seq
            buffer_conteudo.put(info)
            seq += 1
        except socket.timeout:
            continue
        except OSError:
            break

def aguardar_entrada():
    input("Pressione Enter para encerrar o programa...\n")
    stop_event.set()
    print("Encerrando programa...")

    for client_socket in list(clientes_inscritos.keys()):
        try:
            encerrar = Informacao(0, 0, 0)
            client_socket.send(pickle.dumps(encerrar))
            client_socket.close()
        except Exception as e:
            print(e)
            
    clientes_inscritos.clear()

    udp_socket.close()
    tcp_socket.close()

def main():
    thread_geradores = threading.Thread(target=monitorar_geradores)
    thread_clientes = threading.Thread(target=monitorar_clientes, args=(tcp_socket,))
    thread_envio = threading.Thread(target=enviar_para_clientes)

    thread_geradores.start()
    thread_clientes.start()
    thread_envio.start()

    aguardar_entrada()

    thread_geradores.join()
    thread_clientes.join()
    thread_envio.join()

    print("Programa encerrado.")

if __name__ == "__main__":
    main()
