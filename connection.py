import psycopg2


class Conexao:

    def __init__(self, user, password, host, porta, database) -> None:

        self.user = user
        self.password = password
        self.host = host
        self.porta = porta
        self.database = database

    def connection(self):

        connect = psycopg2.connect(
            user=self.user, password=self.password, host=self.host, port=self.porta, database=self.database
        )
        return connect

    def cursor(self):

        if self.connection():
            cursor = self.connection()
            cursor = cursor.cursor()
            return cursor

    def close_cursor_conection(self) -> None:
        if self.connection():
            self.cursor().close()
            self.connection().close()
            print("CONEXÃO COM POSTGRESQL ENCERRADA!!!")
    
    def commit_conection(self):
        if self.connection():
            commit = self.connection()
            commit = commit.commit()
            return commit

