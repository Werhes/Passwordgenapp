import customtkinter as ctk
from tkinter import messagebox
import random
import pywinstyles

# Настройка глобальной темы CustomTkinter
ctk.set_appearance_mode("System")  # Подстраивается под тему Windows (Dark/Light)
ctk.set_default_color_theme("blue")

def generate_password():
    number = '0123456789'
    letter = 'abcdefghijklmnopqrstuvwxyz'
    symbol = '~`@#$%^&*()_+-=[]{}|;:,.<>/?'
    big_letter = letter.upper()
    
    all_chars = list(number + letter + symbol + big_letter)
    password_chars = []
    
    for _ in range(1000):
        # Отслеживаем последние 9 символов
        recent_9_chars = set(password_chars[-9:])
        # Исключаем их из доступных
        available_chars = [c for c in all_chars if c not in recent_9_chars]
        
        chosen_char = random.choice(available_chars)
        password_chars.append(chosen_char)
        
    password = ''.join(password_chars)
    
    # Очистка и вставка (в CustomTkinter немного другой синтаксис)
    password_text.delete("1.0", ctk.END)
    password_text.insert(ctk.END, password)

def copy_to_clipboard():
    password = password_text.get("1.0", ctk.END).strip()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Успешно", "Пароль скопирован в буфер обмена!")

# Настройка главного окна
app = ctk.CTk()
app.title("Генератор паролей")
app.geometry("550x380")
app.resizable(False, False)

# Применение эффекта Mica для Windows 11
pywinstyles.apply_style(app, "mica")

# Заголовок
title_label = ctk.CTkLabel(app, text="Ваш уникальный пароль (1000 символов):", font=ctk.CTkFont(size=15, weight="bold"))
title_label.pack(pady=(20, 10))

# Современное текстовое поле
password_text = ctk.CTkTextbox(
    app, 
    width=500, 
    height=200, 
    wrap="word", 
    font=ctk.CTkFont(family="Consolas", size=13),
    corner_radius=10
)
password_text.pack(pady=10)

# Фрейм для того, чтобы поставить кнопки в один ряд
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

# Главная кнопка (синяя)
generate_btn = ctk.CTkButton(
    button_frame, 
    text="Сгенерировать", 
    font=ctk.CTkFont(size=14, weight="bold"),
    height=35,
    command=generate_password
)
generate_btn.grid(row=0, column=0, padx=10)

# Второстепенная кнопка (серая)
copy_btn = ctk.CTkButton(
    button_frame, 
    text="Скопировать", 
    fg_color=("gray75", "gray30"), # Цвет для светлой и темной темы
    hover_color=("gray65", "gray20"),
    text_color=("black", "white"),
    font=ctk.CTkFont(size=14),
    height=35,
    command=copy_to_clipboard
)
copy_btn.grid(row=0, column=1, padx=10)

# Запуск приложения
app.mainloop()