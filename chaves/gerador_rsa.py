# chaves/gerador_rsa.py
import os
from Crypto.PublicKey import RSA

def gerar_chaves_rsa(tamanho=2048):
    chave = RSA.generate(tamanho)
    chave_privada = chave.export_key()
    chave_publica = chave.publickey().export_key()
    return chave_publica, chave_privada

def salvar_chaves(usuario, chave_publica, chave_privada, diretorio="dados/"):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    with open(f"{diretorio}{usuario}_pub.pem", "wb") as pub_file:
        pub_file.write(chave_publica)
    with open(f"{diretorio}{usuario}_priv.pem", "wb") as priv_file:
        priv_file.write(chave_privada)

# Exemplo de uso
if __name__ == "__main__":
    usuario = "usuario_x"
    chave_publica, chave_privada = gerar_chaves_rsa()
    salvar_chaves(usuario, chave_publica, chave_privada)

