import sqlite3
from sqlite3 import OperationalError
from lib.db import Database


class TeacherManagement(Database):
    """docenten crud"""

    def __init__(self, db_file):
        super().__init__(db_file)

    def get_all_teachers(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM docent WHERE is_verwijderd = 0")
            teacher = cursor.fetchall()
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e

        return teacher
    
    def get_teacher(self, id):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM docent WHERE id = ?", [id])
            teacher = cursor.fetchone()
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e

        return teacher
    
    def get_teacher_json(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.row_factory = sqlite3.Row

            cursor.execute("SELECT * FROM docent WHERE is_verwijderd = 0")
            teacher = cursor.fetchall()

            t_list = []
            for teachers in teacher:
                t_list.append({t: teachers[t] for t in teachers.keys()})
            print(t_list)

            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e

        return t_list
    
    def get_teacher_admin(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.row_factory = sqlite3.Row  # geen idee wat dit is, but whatever works

            cursor.execute(f"SELECT docent.id, docent.voornaam, docent.achternaam, docent.email, "
                           f"docent.is_verwijderd, login.wachtwoord, login.is_admin "
                           f"FROM docent INNER JOIN login "
                           f"ON docent.id=login.docent")
            teacher = cursor.fetchall()

            t_list = []
            for teachers in teacher:
                t_list.append({t: teachers[t] for t in teachers.keys()})
            print(t_list)

            conn.commit()
            conn.close()

        except OperationalError as e:
            print(e)
            raise e
        return t_list

    def add_teacher(self, id, voornaam, achternaam, email):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO docent (id, voornaam, achternaam, email) "
                           "VALUES (?, ?, ?, ?)", [id, voornaam, achternaam, email])
            cursor.execute("INSERT INTO login (email, docent) VALUES (?, ?)", [email, id])
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e

    def edit_teacher(self, voornaam, achternaam, email, id):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"UPDATE docent SET voornaam = ?, achternaam = ?, email = ? "
                           f"WHERE id = ?", [voornaam, achternaam, email, id])
            cursor.execute(f"UPDATE login SET email = (SELECT email FROM docent WHERE id = login.docent)")
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e
    
    def delete_teacher(self, id):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute(f"UPDATE docent SET is_verwijderd = 1 WHERE id = ?", [id])
            conn.commit() 

            conn.close()

        except OperationalError as e:
            print(e)
            raise e
