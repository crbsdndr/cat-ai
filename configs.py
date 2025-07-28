import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.db_host = os.environ.get("DB_LOCALHOST")
        self.db_port = os.environ.get("DB_PORT")
        self.db_name = os.environ.get("DB_DATABASE")
        self.db_user = os.environ.get("DB_USERNAME")
        self.db_password = os.environ.get("DB_PASSWORD")

database = Database()