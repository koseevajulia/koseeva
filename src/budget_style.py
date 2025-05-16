from tkinter import font

# Цвета
BG_COLOR = "#f0f0f0"  # Светло-серый фон
TEXT_COLOR = "#333333" # Темно-серый текст
BUTTON_COLOR = "#4CAF50" # Зеленый цвет для кнопок

# Шрифты
DEFAULT_FONT = font.nametofont("TkDefaultFont")
DEFAULT_FONT.configure(size=12, weight="normal")
TITLE_FONT = font.nametofont("TkDefaultFont")
TITLE_FONT.configure(size=16, weight="bold")
