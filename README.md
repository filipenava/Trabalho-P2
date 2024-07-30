# Projeto de Segurança da Informação

Este é o trabalho da matéria de Segurança da Informação, ministrada pelo professor Ronaldo Toshiaki Oikawa. O objetivo deste trabalho é substituir a nota da P2. Portanto, ele deve ser desenvolvido com o máximo de critério e cuidado, pois a avaliação será rigorosa.

## Critérios de Avaliação

Os seguintes itens impactarão a nota final:
1. **Forma de Implementação:** Divisão entre `def` e `class`.
2. **Criatividade na Solução de Problemas:** Abordagens inovadoras durante a implementação.
3. **Documentação:** Deve seguir os critérios de auditoria e segurança.
4. **Codificação Clara:** Código de fácil compreensão.
5. **Originalidade:** Cópias de código serão penalizadas.
6. **Execução no Servidor:** O programa "server" deve rodar no servidor Linux disponibilizado (RA@200.145.184.166 -p 40665).

## Funcionalidades

1. **Cifra Assimétrica:** Implementação e uso de geração de chaves públicas e privadas (RSA). Gerenciamento dos donos das chaves.
2. **Armazenamento Seguro:** Armazenamento dos usuários e seus pares de chaves em um arquivo TXT criptografado.
3. **Algoritmo Diffie-Hellman:** Implementação para distribuição de chaves.
4. **Função Hash:** Utilização de SHA-256 para gerar uma chave simétrica para a entidade certificadora.
5. **Servidor e Cliente:** Programas que trocam as chaves geradas via sockets.

## Estrutura do Projeto

Trabalho P2/
│
├── cliente/
│   ├── __init__.py
│   ├── cliente.py            # Código do cliente que troca chaves com o servidor
│   └── gerenciamento_chaves.py # Funções para gerenciamento de chaves do cliente
│
├── servidor/
│   ├── __init__.py
│   ├── servidor.py           # Código do servidor que troca chaves com o cliente
│   └── gerenciamento_chaves.py # Funções para gerenciamento de chaves do servidor
│
├── chaves/
│   ├── __init__.py
│   ├── gerador_rsa.py        # Código para gerar as chaves RSA
│   ├── diffie_hellman.py     # Código para implementar Diffie-Hellman
│   ├── hash_sha256.py        # Código para gerar hash SHA-256
│   └── criptografia.py       # Código para criptografar e descriptografar arquivos TXT
│
├── dados/
│   └── usuarios.txt          # Arquivo TXT criptografado para armazenar usuários e suas chaves
│
└── README.md                 # Instruções e documentação do projeto



## Descrição dos Arquivos

### Diretório `cliente/`

- **cliente.py:** Código principal do cliente que se comunica com o servidor via sockets. Gerencia a troca de chaves e a comunicação segura.
- **gerenciamento_chaves.py:** Funções para gerenciar chaves do lado do cliente, como geração, armazenamento e recuperação de chaves.

### Diretório `servidor/`

- **servidor.py:** Código principal do servidor que se comunica com o cliente via sockets. Gerencia a troca de chaves e a comunicação segura.
- **gerenciamento_chaves.py:** Funções para gerenciar chaves do lado do servidor, como geração, armazenamento e recuperação de chaves.

### Diretório `chaves/`

- **gerador_rsa.py:** Implementação da geração de chaves públicas e privadas RSA.
- **diffie_hellman.py:** Implementação do algoritmo Diffie-Hellman para troca de chaves.
- **hash_sha256.py:** Função para gerar um hash SHA-256, utilizado para criar chaves simétricas.
- **criptografia.py:** Funções para criptografar e descriptografar o arquivo TXT que armazena os usuários e suas chaves.

### Diretório `dados/`

- **usuarios.txt:** Arquivo que armazena os usuários e seus pares de chaves de forma criptografada.

## Executando o Projeto

### Requisitos

- Python 3.11.x
- Bibliotecas: `pycryptodome`

### Instruções

1. **Servidor:**
   cd servidor
   python servidor.py

2. **Cliente:**
   cd cliente
   python cliente.py   

### Explicação do Sistema
Este sistema implementa uma entidade certificadora (CA) que gerencia chaves RSA para diferentes usuários. Utilizamos o algoritmo Diffie-Hellman para a troca de chaves e SHA-256 para gerar chaves simétricas que garantem a segurança dos dados armazenados. A comunicação entre cliente e servidor é realizada via sockets, permitindo a troca segura de informações.

### Segurança da Entidade Certificadora
Os pontos seguros do sistema incluem:
- Criptografia RSA: Para garantir a segurança das chaves.
- Diffie-Hellman: Para uma troca segura de chaves.
- Hashing SHA-256: Para integridade e segurança dos dados.
- Criptografia de Arquivos: Para armazenamento seguro das chaves dos usuários.

### Fluxo de Funcionamento

Alice quer conversar com Bob de forma segura. Ela entra em contato com a CA para obter uma chave segura antes de iniciar a comunicação com Bob, seguindo o fluxo apresentado nas aulas.

