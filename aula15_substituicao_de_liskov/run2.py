class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco")


class SqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")


class NoSQLRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco NoSQL")


class DBHandler:
    def alterTable(self):
        print("Alterando tabela em SQL")
