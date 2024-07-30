# chaves/diffie_hellman.py
from Crypto.PublicKey import DSA
from Crypto.Random import random

def diffie_hellman():
    # Usar tamanhos menores para p e g
    p = 23  # Exemplo de um número primo pequeno
    g = 5   # Exemplo de um número gerador pequeno
    a = random.randint(1, p-1)
    A = pow(g, a, p)
    return p, g, a, A

def calcular_chave_secreta(p, g, b, A):
    B = pow(g, b, p)
    chave_secreta = pow(A, b, p)
    return chave_secreta, B

