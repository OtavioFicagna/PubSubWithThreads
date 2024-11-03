from informacoes import Informacao
from queue import Queue
import threading
import socket
import pickle

HOST = '127.0.0.1'
PORT_GERADORES = 5000
PORT_CONSUMIDORES = 8080

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT_GERADORES))

buffer_conteudo = Queue()

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT_CONSUMIDORES))
tcp_socket.listen(5)

clientes_inscritos = {}

print(f'Difusor escutando os geradores na porta {PORT_GERADORES}')
print(f'Difusor escutando os consumidores na porta {PORT_CONSUMIDORES}')

def lidar_com_inscricoes(socket_cliente):
    data = socket_cliente.recv(1024)
    topicos = pickle.loads(data)
    
    if len(topicos) > 0:
        clientes_inscritos[socket_cliente] = topicos
    else:
        del clientes_inscritos[socket_cliente]
        socket_cliente.close()

def monitorar_clientes(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=lidar_com_inscricoes, args=(client_socket))
        client_thread.start()
        
def enviar_para_clientes(info: Informacao):
    for client_socket, topicos in list(clientes_inscritos.items()):
        if info.tipo in topicos:
            try:
                client_socket.send(pickle.dumps(info))
            except:
                del clientes_inscritos[client_socket]

def monitorar_geradores():
    seq = 1
    while True:
        info: Informacao
        msg, _endereco = udp_socket.recvfrom(1024)
        info = pickle.loads(msg)
        info.seq = seq
        print(f"Sequencia: {info.seq} Tipo: {info.tipo} Valor: {info.valor}")
        buffer_conteudo.put(info)
        seq += 1

def main():
    thread_monitora_geradores = threading.Thread(target=monitorar_geradores)
    thread_monitora_geradores.start()
    
    #thread_monitora_consumidores = threading.Thread(target=monitorar_clientes, args=tcp_socket)
    #thread_monitora_consumidores.start()
    
    #thread_envio = threading.Thread(target=enviar_para_clientes, args=(buffer_conteudo.get()))
    #thread_envio.start()
    
if __name__ == "__main__":
    main()