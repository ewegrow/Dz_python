import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Money(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Money")
        self.geometry("700x500")

        self.label_title = ctk.CTkLabel(
            self, text="Покупка телефона", font=("Arial", 20, "bold")
        )
        self.label_title.pack(pady=20)

        self.entry_phone_cost = ctk.CTkEntry(
            self, placeholder_text="Введите стоимость телефона", width=200
        )
        self.entry_phone_cost.pack(pady=5)

        self.entry_financial_reserve_d = ctk.CTkEntry(
            self,
            placeholder_text="Ежедневный взнос",
            width=200,
        )
        self.entry_financial_reserve_d.pack(pady=5)

        self.btn_calc = ctk.CTkButton(self, text="Рассчитать", command=self.calculate)
        self.btn_calc.pack(pady=20)

        self.result_text = ctk.CTkTextbox(self, width=500, height=200)
        self.result_text.pack(pady=10)
        self.result_text.insert(
            "0.0", f"Количество дней для покупки телефона,\n" f"Отобразиться здесь."
        )

    def calculate(self):
        try:

            phone_cost = float(self.entry_phone_cost.get() or 0)
            financial_reserve_d = float(self.entry_financial_reserve_d.get() or 0)

            if financial_reserve_d <= 0:
                raise ValueError

            financial_reserve_w = financial_reserve_d * 6

            total_weeks = phone_cost / financial_reserve_w

            total_days = total_weeks*6

            

            result = (
                f"Стоимость телефона: {round(phone_cost)} BYN\n"
                f"Ежедневный взнос(кроме воскресенья): {financial_reserve_d} BYN\n"
                f"Отложенные деньги с понедельника по субботу(включительно) : {financial_reserve_w} BYN\n"
                f"Количетсво недель, которое потребуется, чтобы накопить: {round(total_weeks, 1)} недель\n"
                f"Количетсво дней, которое потребуется, чтобы накопить: {round(total_days, 1)} дней")

            self.result_text.delete("0.0", "end")
            self.result_text.insert("0.0", result)

        except ValueError:
            self.result_text.delete("0.0", "end")
            self.result_text.insert("0.0", "Ошибка: введите корректные числа")


if __name__ == "__main__":
    app = Money()
    app.mainloop()
