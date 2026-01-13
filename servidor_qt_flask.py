"""
Servidor Flask com interface gráfica em Qt (PyQt5)

- Permite escolher o ficheiro HTML a servir
- Permite definir a porta
- Botões: Ligar / Desligar / Sair
"""

import sys
import threading
import os

from flask import Flask, send_from_directory
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog
)

# ==============================
# VARIÁVEIS GLOBAIS
# ==============================

app = Flask(__name__)
server_thread = None
server_running = False

html_file_path = ""
server_port = 5000

# ==============================
# ROTAS FLASK
# ==============================

@app.route("/")
def index():
    """
    Rota principal.
    Serve o ficheiro HTML escolhido na interface Qt.
    """
    if html_file_path == "":
        return "Nenhum ficheiro HTML configurado."

    pasta = os.path.dirname(html_file_path)
    ficheiro = os.path.basename(html_file_path)

    return send_from_directory(pasta, ficheiro)


# ==============================
# FUNÇÕES DO SERVIDOR
# ==============================

def run_flask():
    """
    Executa o servidor Flask.
    Corre numa thread separada para não bloquear o Qt.
    """
    global server_running
    server_running = True

    print(f"[INFO] Servidor Flask ligado na porta {server_port}")
    app.run(host="0.0.0.0", port=server_port, debug=False, use_reloader=False)

    server_running = False


def start_server():
    """
    Inicia o servidor Flask numa thread.
    """
    global server_thread

    if not server_running:
        server_thread = threading.Thread(target=run_flask, daemon=True)
        server_thread.start()


def stop_server():
    """
    Flask não permite parar facilmente.
    Aqui apenas informamos o utilizador.
    """
    print("[INFO] Para parar o servidor, fecha a aplicação.")
    

# ==============================
# INTERFACE QT
# ==============================

class JanelaServidor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Servidor Flask com Qt")
        self.setGeometry(100, 100, 500, 200)

        # --------------------------
        # COMPONENTES
        # --------------------------

        self.label_html = QLabel("Ficheiro HTML:")
        self.caixa_html = QLineEdit()
        self.botao_html = QPushButton("Escolher")

        self.label_porta = QLabel("Porta do servidor:")
        self.caixa_porta = QLineEdit("5000")

        self.botao_ligar = QPushButton("Ligar")
        self.botao_desligar = QPushButton("Desligar")
        self.botao_sair = QPushButton("Sair")

        # --------------------------
        # LAYOUTS
        # --------------------------

        layout_html = QHBoxLayout()
        layout_html.addWidget(self.caixa_html)
        layout_html.addWidget(self.botao_html)

        layout_botoes = QHBoxLayout()
        layout_botoes.addWidget(self.botao_ligar)
        layout_botoes.addWidget(self.botao_desligar)
        layout_botoes.addWidget(self.botao_sair)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.label_html)
        layout_principal.addLayout(layout_html)
        layout_principal.addWidget(self.label_porta)
        layout_principal.addWidget(self.caixa_porta)
        layout_principal.addLayout(layout_botoes)

        self.setLayout(layout_principal)

        # --------------------------
        # SINAIS
        # --------------------------

        self.botao_html.clicked.connect(self.escolher_html)
        self.botao_ligar.clicked.connect(self.ligar_servidor)
        self.botao_desligar.clicked.connect(self.desligar_servidor)
        self.botao_sair.clicked.connect(self.close)

    # ==========================
    # FUNÇÕES DA INTERFACE
    # ==========================

    def escolher_html(self):
        """
        Abre um diálogo para escolher o ficheiro HTML.
        """
        global html_file_path

        ficheiro, _ = QFileDialog.getOpenFileName(
            self, "Escolher ficheiro HTML", "", "HTML (*.html)"
        )

        if ficheiro:
            html_file_path = ficheiro
            self.caixa_html.setText(ficheiro)

    def ligar_servidor(self):
        """
        Lê a porta e inicia o servidor Flask.
        """
        global server_port

        try:
            server_port = int(self.caixa_porta.text())
            start_server()
        except ValueError:
            print("[ERRO] Porta inválida.")

    def desligar_servidor(self):
        """
        Apenas informa (limitação do Flask).
        """
        stop_server()


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    app_qt = QApplication(sys.argv)
    janela = JanelaServidor()
    janela.show()
    sys.exit(app_qt.exec_())
