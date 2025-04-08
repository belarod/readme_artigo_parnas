from cod_modularizado import MusicaDoBanco, ReproduzirMusica

def main():
    # Dados fictícios
    musica_id = 1
    nome_musica = "Minha Canção Favorita"
    codigo = "X123"
    categoria = "Pop"
    caminho_arquivo = "/musicas/favorita.mp3"

    # Dados do banco fictício
    db_nome = "MusicasDB"
    db_caminho = "/banco/musicas.db"
    db_tipo = "SQLite"
    db_senha = "1234"

    musica = MusicaDoBanco(
        db_name=db_nome,
        db_path=db_caminho,
        db_type=db_tipo,
        db_password=db_senha,
        musica_id=musica_id,
        name=nome_musica,
        cod=codigo,
        categoria=categoria
        )

    # Fluxo de execução
    musica.buscar()
    musica.decodificar()

    # Reproduzindo a música
    player = ReproduzirMusica(musica_id, nome_musica, caminho_arquivo)
    player.reproduzir()

if __name__ == "__main__":
    main()