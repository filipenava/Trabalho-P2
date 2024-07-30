# chaves/hash_sha256.py
import hashlib

def gerar_hash_sha256(mensagem):
    hash_object = hashlib.sha256(mensagem.encode())
    hash_digest = hash_object.hexdigest()
    return hash_digest

# Exemplo de uso
if __name__ == "__main__":
    mensagem = "exemplo_mensagem"
    hash_digest = gerar_hash_sha256(mensagem)
    print(f"Hash SHA-256: {hash_digest}")

