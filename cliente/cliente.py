# cliente/cliente.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
import socket
from chaves.diffie_hellman import diffie_hellman, calcular_chave_secreta

def cliente():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))
    print("Cliente conectado ao servidor.")

    try:
        p, g, a, A = diffie_hellman()
        mensagem = f"{p},{g},{A}"
        if len(mensagem) > 4096:
            raise ValueError("A mensagem é muito longa para ser enviada.")
        print(f"Mensagem enviada: {mensagem}")
        s.send(mensagem.encode())
        
        data = s.recv(4096).decode()
        print(f"Dados recebidos do servidor: {data}")
        if not data:
            raise ValueError("Nenhum dado recebido do servidor.")
        
        B = int(data)
        chave_secreta = calcular_chave_secreta(p, g, a, B)
        print(f"Chave secreta compartilhada: {chave_secreta}")
    except Exception as e:
        print(f"Erro durante a comunicação: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    cliente()
