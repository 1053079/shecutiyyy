import sqlite3
from sqlite3 import OperationalError
from lib.db import Database


class Login(Database):
    """dit zou de login moeten doen maar (insert shrugging emoji)"""

    def __init__(self, db_file):
        super().__init__(db_file)

    def login_user(self, usn, pwd):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM login WHERE email = ? AND wachtwoord = ?",[usn, pwd])
            user = cursor.fetchone()
            print(user)
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e
        return user
