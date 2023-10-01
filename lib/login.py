import sqlite3
from flask_bcrypt import Bcrypt
from sqlite3 import OperationalError
from lib.db import Database


class Login(Database):
    """dit zou de login moeten doen maar (insert shrugging emoji)"""

    def __init__(self, db_file):
        super().__init__(db_file)

    def login_user(self, usn, password):
        try:
            conn = sqlite3.connect(self.db_file)
            self.bcrypt = Bcrypt()
            cursor = conn.cursor()
            
            cursor.execute("SELECT wachtwoord FROM login WHERE email = ?",[usn])
            user = cursor.fetchone()
            print(user)
            if user:
                password = password
                stored_hashed_password = user[0]
                print('password ' + password)
                print('stored hash pw ' + stored_hashed_password)
                if self.bcrypt.check_password_hash(stored_hashed_password, password):
                    print('you have successfully logged in as ' + usn)
                    conn.commit() 
                    conn.close()
                    return user
                else:
                    print('Incorrect username or password')
                    conn.commit() 
                    conn.close()
                    return None
            else:
                print(user)
                conn.commit() 
                conn.close()

        except OperationalError as e:
            print(e)
            raise e
        return user
