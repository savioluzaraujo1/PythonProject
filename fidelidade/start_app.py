import os
import subprocess
import webbrowser
import time

# Configurar o caminho do arquivo manage.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MANAGE_PY = os.path.join(BASE_DIR, "manage.py")

# Endereço do servidor
SERVER_URL = "http://127.0.0.1:8000/"

def start_server():
    # Comando para iniciar o servidor Django
    command = ["python", MANAGE_PY, "runserver"]
    # Iniciar o servidor em um subprocesso
    subprocess.Popen(command)
    # Esperar alguns segundos para garantir que o servidor inicie
    time.sleep(3)
    # Abrir o navegador no endereço do servidor
    webbrowser.open(SERVER_URL)

if __name__ == "__main__":
    start_server()
