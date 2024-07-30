# servidor/servidor.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import socket
from Crypto.Random import random
from chaves.diffie_hellman import calcular_chave_secreta

def servidor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 9999))
    s.listen(1)
    print("Servidor aguardando conexões...")

    conn, addr = s.accept()
    print(f"Conectado por {addr}")

    try:
        data = conn.recv(4096).decode()
        print(f"Dados recebidos: {data}")
        if not data:
            raise ValueError("Nenhum dado recebido do cliente.")
        
        partes = data.split(",")
        if len(partes) != 3:
            raise ValueError("Mensagem recebida com formato incorreto.")
        
        p, g, A = map(int, partes)
        b = random.StrongRandom().randint(1, p-1)
        chave_secreta, B = calcular_chave_secreta(p, g, b, A)
        
        conn.send(f"{B}".encode())
        print(f"Chave secreta compartilhada: {chave_secreta}")
    except Exception as e:
        print(f"Erro durante a comunicação: {e}")
    finally:
        conn.close()
        s.close()

if __name__ == "__main__":
    servidor()