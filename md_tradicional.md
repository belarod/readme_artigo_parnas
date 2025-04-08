```python
# Módulo 1 - Entrada
def receber_input_do_usuario(usuario_id: int, preferencia: str):
    if preferencia == "recomendar":
        print("📥 Usuário clicou em 'Ver recomendações'")
        return usuario_id
    elif preferencia == "rock":
        print("📥 Usuário clicou em 'Ver rock'")
        return usuario_id
    elif preferencia == "pop":  
        print("📥 Usuário clicou em 'Ver pop'")
        return usuario_id
    #etc... outros tipos de preferências

# Módulo 2 - Processamento
def processar_pedido(usuario_id: int, preferencia: str):
    print(f"⚙️ Processando pedido para o usuário {usuario_id}")
    db = "db_musicas"
    cur = "conexao_db"
    musica = "musica selecionada"
    musica_decodificada = "musica_decodificada"
    is_assinante = verificar_assinatura(usuario_id)
    
    def verificar_assinatura(usuario_id: int):
        if usuario_id.assinatura():
            print(f"🔑 Verificando assinatura do usuário {usuario_id}")
            return True
        else:
            print(f"❌ Usuário {usuario_id} não possui assinatura.")
            return False
    
    if is_assinante:
        cur.open() 
        print(f"🔍 Buscando {musica} {preferencia} no banco de dados '{db}' para o usuário {usuario_id}")
        print("🔄 Decodificando o áudio")
        return musica_decodificada
        cur.close()
    else:
        print("❌ Acesso negado. Você não possui uma assinatura ativa.")
        return None
    

# Módulo 3 - Saída
def tocar_audio(musica_decodificada):
    url = f"https://streaming.service/{musica_decodificada}"
    print(f"🎧 Tocando áudio: {musica_decodificada}")
    return url
```