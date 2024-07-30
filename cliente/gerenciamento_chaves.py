# cliente/gerenciamento_chaves.py ou servidor/gerenciamento_chaves.py
import os
from chaves.gerador_rsa import gerar_chaves_rsa, salvar_chaves
from chaves.criptografia import criptografar_arquivo, descriptografar_arquivo
from chaves.hash_sha256 import gerar_hash_sha256

def armazenar_usuario_chaves(usuario, diretorio="dados/"):
    chave_publica, chave_privada = gerar_chaves_rsa()
    conteudo = f"Usuário: {usuario}\nChave Pública: {chave_publica.decode()}\nChave Privada: {chave_privada.decode()}"
    chave_simetrica = gerar_hash_sha256(usuario).encode()[:16]
    conteudo_criptografado = criptografar_arquivo(conteudo, chave_simetrica)
    with open(f"{diretorio}{usuario}.txt", "w") as arquivo:
        arquivo.write(conteudo_criptografado)

def recuperar_usuario_chaves(usuario, diretorio="dados/"):
    chave_simetrica = gerar_hash_sha256(usuario).encode()[:16]
    with open(f"{diretorio}{usuario}.txt", "r") as arquivo:
        conteudo_criptografado = arquivo.read()
    conteudo_descriptografado = descriptografar_arquivo(conteudo_criptografado, chave_simetrica)
    return conteudo_descriptografado

# Exemplo de uso
if __name__ == "__main__":
    usuario = "usuario_x"
    armazenar_usuario_chaves(usuario)
    conteudo = recuperar_usuario_chaves(usuario)
    print(f"Conteúdo descriptografado do arquivo: {conteudo}")
