from cliente.gerenciamento_chaves import armazenar_usuario_chaves, recuperar_usuario_chaves
usuario = "usuario_teste"
armazenar_usuario_chaves(usuario)
conteudo = recuperar_usuario_chaves(usuario)
print(f"Conteúdo descriptografado do arquivo: {conteudo}")
