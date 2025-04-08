class Musica: #classe de estrutura de dado
    def __init__(self, musica_id, name, cod, categoria):
        self.musica_id = musica_id
        self.name = name
        self.cod = cod
        self.categoria = categoria

class ReproduzirMusica(Musica): #classe filha funcional
    def __init__(self, musica_id, name, path):
        super().__init__(musica_id, name, path)
        
    def reproduzir(self):
        print(f"Playing '{self.name}' from {self.path}")
        
class BancoDeDadosMusicas(Musica): #classe de estrutura de dado
    def __init__(self, db_name, db_path, db_type, db_password, musica_id, name, cod, categoria):
        super().__init__(musica_id, name, cod, categoria)
        self.db_password = db_password
        self.db_type = db_type
        self.db_path = db_path
        self.db_name = db_name

class MusicaDoBanco(BancoDeDadosMusicas): #classe filha funcional
    def __init__(self, db_name, db_path, db_type, db_password, musica_id, name, cod, categoria):
        super().__init__(db_name, db_path, db_type, db_password, musica_id, name, cod, categoria)
        self.db_name = db_name
        self.db_path = db_path
        self.db_type = db_type
        self.db_password = db_password   
             
    def conectar(self):
        print(f"Connecting to {self.db_name} database")
        
    def desconectar(self):
        print(f"Disconnecting from {self.db_name} database")
        
    def decodificar(self):
        print(f"Decoding music '{self.name}' from {self.cod}")
        
    def buscar(self):
        print(f"Searching for music '{self.name}' (ID: {self.musica_id}, Code: {self.cod}, Category: {self.categoria}) in {self.db_path}, database type: {self.db_type}")
        
#ISSO É APENAS PARA FINS DIDATICOS, MANEIRA CORRETA SERIA NÃO PASSAR NENHUM PARAMETRO E USAR FUNÇÕES ABSTRATAS P INTERFACES