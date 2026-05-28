import math
import emoji
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk


def credit_game():
    try:

        s = float(entry_s.get())
        i = float(entry_i.get())
        n = float(entry_n.get())

        months = n * 12
        p = (i / 100) / 12
        momthly_payment = s * (p * (1 + p) ** months) / ((1 + p) ** months - 1)
        total_payment = momthly_payment * months
        overpayment = (momthly_payment * months) - s

        result = (
            f"💰 Размер ежемесячной выплаты составит:{round(momthly_payment, 2)}BYN\n"
            f"💰 Общая сумма выплаты банку составит:{round(total_payment, 2)}BYN\n"
            f"💰 Сумма переплаты:{round(overpayment, 2)}BYN\n"
            f"⛔ Восстановление нервной системы: НИКОГДА"
        )
        label_result.config(text=result)

    except ValueError:
        messagebox.showerror("Ошибка: Введены нечисловые данные. Попробуйте снова.")


root = tk.Tk()
root.title("credit game")
img = Image.open("scam.PNG")
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
root.geometry("400x400+700+400")
tk.Label(root, text="Заскамим мамонта:", font=("Arial", 12, "bold")).pack(
    pady=5
)
tk.Label(root, text="Сумма кредита:").pack()
entry_s = tk.Entry()
entry_s.pack()

tk.Label(root, text="Годовая процентная ставка:").pack()
entry_i = tk.Entry(root)
entry_i.pack()

tk.Label(root, text="Срок кредита:").pack()
entry_n = tk.Entry(root)
entry_n.pack()


btn_credit_game = tk.Button(root, text="Произвести рассчет", command=credit_game)
btn_credit_game.pack(pady=15)


label_result = tk.Label(root, text="", justify="left", fg="purple")
label_result.pack()

root.mainloop()
