# src/views.py
import tkinter as tk
from tkinter import ttk
from src.budget_style import BG_COLOR, TEXT_COLOR, BUTTON_COLOR, TITLE_FONT, DEFAULT_FONT

class FamilyBudgetView(tk.Frame):
    def __init__(self, parent, family_members, db_file):
        super().__init__(parent)
        self.parent = parent
        self.family_members = family_members
        self.db_file = db_file  

        self.configure(bg=BG_COLOR)
        self.parent.title("Учет Семейного Бюджета")  
       
        try:
            self.parent.iconbitmap("resources/icon.ico") 
        except:
            print ("Не удалось загрузить иконку")

        self.create_widgets()

    def create_widgets(self):
       
        self.title_label = tk.Label(self, text="Список Членов Семьи", font=TITLE_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.title_label.pack(pady=10)

        self.family_member_list = ttk.Treeview(self, columns=("ID", "Имя", "Фамилия", "Дата рождения", "Email", "Телефон"), show="headings", height=10, style="Custom.Treeview") 

        self.family_member_list.heading("ID", text="ID")
        self.family_member_list.heading("Имя", text="Имя")
        self.family_member_list.heading("Фамилия", text="Фамилия")
        self.family_member_list.heading("Дата рождения", text="Дата рождения")
        self.family_member_list.heading("Email", text="Email")
        self.family_member_list.heading("Телефон", text="Телефон")

        self.family_member_list.column("ID", width=50)
        self.family_member_list.column("Имя", width=100)
        self.family_member_list.column("Фамилия", width=100)
        self.family_member_list.column("Дата рождения", width=100)
        self.family_member_list.column("Email", width=150)
        self.family_member_list.column("Телефон", width=100)

        for member in self.family_members:
            self.family_member_list.insert("", "end", values=(
                member.member_id,
                member.first_name,
                member.last_name,
                member.birth_date,
                member.email,
                member.phone_number,
            ))

        self.family_member_list.pack(pady=10)

        self.budget_label = tk.Label(self, text="Состояние бюджета: Не рассчитывается (требуется расширение)", font=DEFAULT_FONT, bg=BG_COLOR, fg=TEXT_COLOR)
        self.budget_label.pack(pady=10)

      
        self.add_button = tk.Button(self, text="Добавить", font=DEFAULT_FONT, bg=BUTTON_COLOR, fg="white")  
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.edit_button = tk.Button(self, text="Редактировать", font=DEFAULT_FONT, bg=BUTTON_COLOR, fg="white")  
        self.edit_button.pack(side=tk.LEFT, padx=5)

style = ttk.Style()
style.theme_use("default")
style.configure("Custom.Treeview",
                background=BG_COLOR,
                fieldbackground=BG_COLOR,
                foreground=TEXT_COLOR,
                font=DEFAULT_FONT
                )
style.configure("Custom.Treeview.Heading",
                background=BG_COLOR,
                foreground=TEXT_COLOR,
                font=DEFAULT_FONT
                )
