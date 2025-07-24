import psycopg2
import os

class Database:
    def __init__(self):
        db_host = "localhost"
        db_port = 5432
        db_name = "catai"
        db_user = "postgres"
        db_password = os.environ.get("DB_PASSWORD")

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
