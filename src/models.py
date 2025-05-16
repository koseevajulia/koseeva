# src/models.py
class FamilyMember:
    def __init__(self, member_id, first_name, last_name, birth_date, email, phone_number):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.phone_number = phone_number
