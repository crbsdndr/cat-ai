from app import configs
import psycopg2

class Database:
    def __init__(self):
        db_host = configs.database.db_host
        db_port = configs.database.db_port
        db_name = configs.database.db_name
        db_user = configs.database.db_user
        db_password = configs.database.db_password

        self.connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()
