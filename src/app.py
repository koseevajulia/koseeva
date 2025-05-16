# src/app.py
import tkinter as tk
from src.views import FamilyBudgetView
from src.controllers import get_family_members

if __name__ == "__main__":
    db_file = 'db/family_budget.db' 
    root = tk.Tk()
    root.geometry("800x600")
    family_members = get_family_members(db_file)
    app = FamilyBudgetView(root, family_members, db_file)
    app.pack(expand=True, fill="both")  

    root.mainloop()
