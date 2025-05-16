# src/controllers.py
import sqlite3
from src.models import FamilyMember 

def get_family_members(db_file):
    """
    Получает список членов семьи из базы данных.
    """
    family_members = []
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT member_id, first_name, last_name, birth_date, email, phone_number FROM FamilyMembers")
        rows = cursor.fetchall()
        for row in rows:
            member_id, first_name, last_name, birth_date, email, phone_number = row
            family_members.append(FamilyMember(member_id, first_name, last_name, birth_date, email, phone_number)) # Используем модель
    except sqlite3.Error as e:
        print(f"Ошибка при получении данных из БД: {e}")
    finally:
        if conn:
            conn.close()
    return family_members
