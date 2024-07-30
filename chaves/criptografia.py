# chaves/criptografia.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def criptografar_arquivo(conteudo, chave):
    cipher = AES.new(chave, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(conteudo.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def descriptografar_arquivo(conteudo_criptografado, chave):
    dados = base64.b64decode(conteudo_criptografado)
    nonce = dados[:16]
    ciphertext = dados[16:]
    cipher = AES.new(chave, AES.MODE_EAX, nonce=nonce)
    conteudo_descriptografado = cipher.decrypt(ciphertext).decode()
    return conteudo_descriptografado

# Exemplo de uso
if __name__ == "__main__":
    chave = get_random_bytes(16)
    conteudo = "Exemplo de conteúdo para criptografar"
    conteudo_criptografado = criptografar_arquivo(conteudo, chave)
    conteudo_descriptografado = descriptografar_arquivo(conteudo_criptografado, chave)
    print(f"Conteúdo descriptografado: {conteudo_descriptografado}")

