import socket
import threading
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_consumidor import Ui_MainWindow
from informacoes import Informacao
import sys
import pickle

class Consumidor(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Consumidor")

        self.server_host = '127.0.0.1'
        self.server_port = 8080
        self.client_socket = None
        self.subscriptions = {"esportes": False, "novidades": False, "eletronicos": False, 
                              "politicas": False, "negocios": False, "viagens": False}
        self.subs = set()
        self.subs.add(0)
        self.running = True

        self.btn_esportes.clicked.connect(lambda: self.toggle_subscription("esportes"))
        self.btn_novidades.clicked.connect(lambda: self.toggle_subscription("novidades"))
        self.btn_eletronicos.clicked.connect(lambda: self.toggle_subscription("eletronicos"))
        self.btn_politicas.clicked.connect(lambda: self.toggle_subscription("politicas"))
        self.btn_negocios.clicked.connect(lambda: self.toggle_subscription("negocios"))
        self.btn_viagens.clicked.connect(lambda: self.toggle_subscription("viagens"))

        self.connection_thread = threading.Thread(target=self.connect_to_server, daemon=True)
        self.connection_thread.start()

    def connect_to_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.server_host, self.server_port))
            print("Conexão estabelecida com o servidor")

            self.receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            self.receive_thread.start()

        except Exception as e:
            print("Erro ao conectar ao servidor:", e)
            self.show_error_message(f"Erro ao conectar ao servidor: {e}")

    def toggle_subscription(self, category):
        if category == "esportes":
            if not self.subscriptions["esportes"]:
                self.subs.add(1)
                self.send_subscription()
                self.subscriptions["esportes"] = True
                self.btn_esportes.setText("Parar")
                self.textEsportes.append("Inscrito na categoria de esportes.")
            else:
                self.subs.remove(1)
                self.send_subscription()
                self.subscriptions["esportes"] = False
                self.btn_esportes.setText("Inscrever-se")
                self.textEsportes.append("Inscrição cancelada na categoria de esportes.")
        elif category == "novidades":
            if not self.subscriptions["novidades"]:
                self.subs.add(2)
                self.send_subscription()
                self.subscriptions["novidades"] = True
                self.btn_novidades.setText("Parar")
                self.textNovidades.append("Inscrito na categoria de novidades.")
            else:
                self.subs.remove(2)
                self.send_subscription()
                self.subscriptions["novidades"] = False
                self.btn_novidades.setText("Inscrever-se")
                self.textNovidades.append("Inscrição cancelada na categoria de novidades.")
        elif category == "eletronicos":
            if not self.subscriptions["eletronicos"]:
                self.subs.add(3)
                self.send_subscription()
                self.subscriptions["eletronicos"] = True
                self.btn_eletronicos.setText("Parar")
                self.textEletronicos.append("Inscrito na categoria de eletronicos.")
            else:
                self.subs.remove(3)
                self.send_subscription()
                self.subscriptions["eletronicos"] = False
                self.btn_eletronicos.setText("Inscrever-se")
                self.textEletronicos.append("Inscrição cancelada na categoria de eletronicos.")
        elif category == "politicas":
            if not self.subscriptions["politicas"]:
                self.subs.add(4)
                self.send_subscription()
                self.subscriptions["politicas"] = True
                self.btn_politicas.setText("Parar")
                self.textPoliticas.append("Inscrito na categoria de politicas.")
            else:
                self.subs.remove(4)
                self.send_subscription()
                self.subscriptions["politicas"] = False
                self.btn_politicas.setText("Inscrever-se")
                self.textPoliticas.append("Inscrição cancelada na categoria de politicas.")
        elif category == "negocios":
            if not self.subscriptions["negocios"]:
                self.subs.add(5)
                self.send_subscription()
                self.subscriptions["negocios"] = True
                self.btn_negocios.setText("Parar")
                self.textNegocios.append("Inscrito na categoria de negocios.")
            else:
                self.subs.remove(5)
                self.send_subscription()
                self.subscriptions["negocios"] = False
                self.btn_negocios.setText("Inscrever-se")
                self.textNegocios.append("Inscrição cancelada na categoria de negocios.")
        elif category == "viagens":
            if not self.subscriptions["viagens"]:
                self.subs.add(6)
                self.send_subscription()
                self.subscriptions["viagens"] = True
                self.btn_viagens.setText("Parar")
                self.textViagens.append("Inscrito na categoria de viagens.")
            else:
                self.subs.remove(6)
                self.send_subscription()
                self.subscriptions["viagens"] = False
                self.btn_viagens.setText("Inscrever-se")
                self.textViagens.append("Inscrição cancelada na categoria de viagens.")

    def send_subscription(self):
        try:
            inscricao = pickle.dumps(self.subs)
            self.client_socket.sendall(inscricao)
        except Exception as e:
            print("Erro ao enviar mensagem de inscrição:", e)
            self.show_error_message(f"Erro ao enviar mensagem de inscrição: {e}")

    def receive_messages(self):
        while self.running:
            try:
                msg = self.client_socket.recv(1024)
                if msg:
                    info : Informacao = pickle.loads(msg)
                    if info.seq == 0 and info.tipo == 0 and info.valor == 0:
                        self.show_error_message(f"Servidor foi encerrado inesperadamente!")
                        break
                    fstring = f"Sequência: {info.seq} | Valor: {info.valor}"
                    if info.tipo == 1:
                        self.textEsportes.append(fstring)
                    elif info.tipo == 2:
                        self.textNovidades.append(fstring)
                    elif info.tipo == 3:
                        self.textEletronicos.append(fstring)
                    elif info.tipo == 4:
                        self.textPoliticas.append(fstring)
                    elif info.tipo == 5:
                        self.textNegocios.append(fstring)
                    elif info.tipo == 6:
                        self.textViagens.append(fstring)
            except Exception as e:
                if self.running:
                    print("Erro ao receber mensagem do servidor:", e)
                break

    def show_error_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Erro de Conexão")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setStandardButtons(QMessageBox.Close)
        msg_box.buttonClicked.connect(self.close_application)
        msg_box.exec_()

    def close_application(self):
        self.close()

    def closeEvent(self, event):
        self.running = False
        if self.client_socket:
            try:
                self.subs.clear()
                self.send_subscription()
                self.client_socket.close()
                print("Conexão fechada com o servidor")
            except Exception:
                pass
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Consumidor()
    window.show()
    app.exec_()