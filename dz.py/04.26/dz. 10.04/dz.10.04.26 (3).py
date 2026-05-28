import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import math

def interstellar():
    try:
        
        r1 = float(entry_radius_1.get())
        v1 = float(entry_orbital_speed_1.get())
        r2 = float(entry_radius_2.get())
        v2 = float(entry_orbital_speed_2.get())

        if v1 <= 0 or v2 <= 0:
            messagebox.showerror("Ошибка", "Скорость должна быть больше нуля!")
            return
        
        
        year_1 = (2 * math.pi * r1) / v1
        year_2 = (2 * math.pi * r2) / v2

        is_longer = "Да" if year_1 > year_2 else "Нет"

        result = (f"Год на 1-й планете: {round(year_1, 2)} ч.\n"
                  f"Год на 2-й планете: {round(year_2, 2)} ч.\n"
                  f"На первой планете год длиннее? {is_longer}")
        
        label_result.configure(text=result)
 
    except ValueError:
       messagebox.showerror("Ошибка", "Введите корректные числовые значения.")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Интерстеллар")
root.geometry("400x600")


try:
    img = Image.open('alert.PNG')
    photo = ImageTk.PhotoImage(img)
    root.wm_iconphoto(False, photo)
except:
    pass


ctk.CTkLabel(root, text="Планета №1", font=('Arial', 14, 'bold'), text_color="#5dade2").pack(pady=(20, 5))
ctk.CTkLabel(root, text="Радиус орбиты (млн. км.):").pack()
entry_radius_1 = ctk.CTkEntry(root, width=200)
entry_radius_1.pack(pady=5)

ctk.CTkLabel(root, text="Орбитальная скорость (км/ч):").pack()
entry_orbital_speed_1 = ctk.CTkEntry(root, width=200)
entry_orbital_speed_1.pack(pady=5)

ctk.CTkLabel(root, text="Планета №2", font=('Arial', 14, 'bold'), text_color="#e10add").pack(pady=(20, 5))
ctk.CTkLabel(root, text="Радиус орбиты (млн. км.):").pack()
entry_radius_2 = ctk.CTkEntry(root, width=200)
entry_radius_2.pack(pady=5)

ctk.CTkLabel(root, text="Орбитальная скорость (км/ч):").pack()
entry_orbital_speed_2 = ctk.CTkEntry(root, width=200)
entry_orbital_speed_2.pack(pady=5)

btn_interstellar = ctk.CTkButton(root, text="Сравнить время", 
command=interstellar, 
fg_color="#4503e0", 
hover_color="#14375e")
btn_interstellar.pack(pady=30)


res_frame = ctk.CTkFrame(root, fg_color="transparent", border_width=1, border_color="purple")
res_frame.pack(pady=10, padx=30, fill="x")

label_result = ctk.CTkLabel(res_frame, text="Результаты расчета", font=('Arial', 12, 'italic'), text_color="mediumpurple")
label_result.pack(pady=15)

root.mainloop()
