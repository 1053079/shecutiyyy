import sqlite3
from sqlite3 import OperationalError
from lib.db import Database


class ClassManagement(Database):
    """klassen crud"""

    def __init__(self, db_file):
        super().__init__(db_file)

    def get_class(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM klas")
            classes = cursor.fetchall()
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e
        return classes

    def get_enrollment(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM enrollment")
            enrollment = cursor.fetchall()
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e
        return enrollment
    
    def add_class(self, klas):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"INSERT INTO klas (id) VALUES (?)", [klas])
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e

    def edit_class(self, klas):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"UPDATE klas SET id = ? WHERE id = ?", [klas])
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e

    def delete_class(self, klas):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM klas WHERE id = ?", [klas])
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e
