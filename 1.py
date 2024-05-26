from tkinter import font
import tkinter as tk
root = tk.Tk()
root.title("Пример использования шрифта Rockwell Extra Bold")

available_fonts = list(font.families())
if "Rostov" in available_fonts:
    print("Шрифт 'Rockwell Extra Bold' доступен.")
custom_font = font.Font(family="Rostov", size=20)

# Создаем метку с использованием шрифта
label = tk.Label(root, text="Привет, мир!", font=custom_font)
label.pack(pady=20)

# Запускаем главный цикл приложения
root.mainloop()