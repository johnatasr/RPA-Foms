import sqlite3
from models import input


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = None

    def start(self) -> None:
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS input (id INTEGER PRIMARY KEY, name VARCHAR(200), key VARCHAR(200), value VARCHAR(4)"\
        )
        self.connection.commit()
        self.connection.close()



