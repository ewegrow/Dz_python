import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

def credit_game():
    try:
        
        s = float(entry_s.get())
        i = float(entry_i.get())
        n = float(entry_n.get())

        months = n * 12
        p = (i / 100) / 12
        
       
        monthly_payment = s * (p * (1 + p) ** months) / ((1 + p) ** months - 1)
        total_payment = monthly_payment * months
        overpayment = total_payment - s

        result = (
            f"💰 Ежемесячный платеж: {round(monthly_payment, 2)} BYN\n"
            f"💰 Общая сумма: {round(total_payment, 2)} BYN\n"
            f"💰 Переплата: {round(overpayment, 2)} BYN\n"
            f"⛔ Нервная система: ВОССТАНОВЛЕНИЮ НЕ ПОДЛЕЖИТ"
        )
        label_result.configure(text=result)

    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа! Мамонт сам себя не заскамит.")
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Процентная ставка не может быть 0.")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Credit Game")
root.geometry("450x450")


try:
    img = Image.open("scam.PNG")
    photo = ImageTk.PhotoImage(img)
    root.wm_iconphoto(False, photo)
except:
    pass 


ctk.CTkLabel(root, text="Заскамим мамонта", font=("Arial", 16, "bold")).pack(pady=15)

ctk.CTkLabel(root, text="Сумма кредита (BYN):").pack()
entry_s = ctk.CTkEntry(root)
entry_s.pack(pady=5)

ctk.CTkLabel(root, text="Годовая ставка (%):").pack()
entry_i = ctk.CTkEntry(root)
entry_i.pack(pady=5)

ctk.CTkLabel(root, text="Срок (в годах):").pack()
entry_n = ctk.CTkEntry(root)
entry_n.pack(pady=5)

btn_calc = ctk.CTkButton(root, text="Рассчитать ущерб", command=credit_game)
btn_calc.pack(pady=20)

label_result = ctk.CTkLabel(root, text="", justify="left", text_color="violet", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()