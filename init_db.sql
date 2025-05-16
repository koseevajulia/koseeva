
CREATE TABLE FamilyMembers (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE,
    email VARCHAR(255),
    phone_number VARCHAR(20)
);
