import csv
import json
import os
import customtkinter as ctk


ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

JSON_FILE = "employees.json"
CSV_FILE = "employees.csv"


def load_json_data():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


class EmployeeApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Управление базой сотрудников")
        self.geometry("700x550")
        self.resizable(False, False)

        self.tabview = ctk.CTkTabview(self, width=660, height=510)
        self.tabview.pack(padx=20, pady=10)

        self.tabview.add("База и Поиск")
        self.tabview.add("Добавление сотрудника")
        self.tabview.add("Аналитика и Фильтры")

        self.setup_tab_search(self.tabview.tab("База и Поиск"))
        self.setup_tab_add(self.tabview.tab("Добавление сотрудника"))
        self.setup_tab_analytics(self.tabview.tab("Аналитика и Фильтры"))

    def setup_tab_search(self, tab):
        self.btn_csv = ctk.CTkButton(
            tab,
            text="Синхронизировать и сохранить в CSV",
            command=self.json_to_csv,
        )
        self.btn_csv.pack(pady=10)

        search_frame = ctk.CTkFrame(tab)
        search_frame.pack(fill="x", padx=10, pady=10)

        self.entry_search_name = ctk.CTkEntry(
            search_frame, placeholder_text="Введите имя сотрудника...", width=350
        )
        self.entry_search_name.pack(side="left", padx=10, pady=10)

        self.btn_search = ctk.CTkButton(
            search_frame, text="Найти", command=self.find_employee
        )
        self.btn_search.pack(side="right", padx=10, pady=10)

        self.txt_output = ctk.CTkTextbox(tab, width=620, height=260)
        self.txt_output.pack(pady=10)
        self.show_log("[+] Приложение запущено. Нажмите 'Найти' с пустым полем для вывода всех сотрудников.")

    def setup_tab_add(self, tab):
        # Форма ввода данных
        form_frame = ctk.CTkFrame(tab, fg_color="transparent")
        form_frame.pack(pady=10)

        ctk.CTkLabel(form_frame, text="ФИО:").grid(
            row=0, column=0, sticky="w", pady=5, padx=5
        )
        self.ent_name = ctk.CTkEntry(form_frame, width=250)
        self.ent_name.grid(row=0, column=1, pady=5, padx=5)

        ctk.CTkLabel(form_frame, text="Дата рождения (ДД.ММ.ГГГГ):").grid(
            row=1, column=0, sticky="w", pady=5, padx=5
        )
        self.ent_birth = ctk.CTkEntry(form_frame, width=250)
        self.ent_birth.grid(row=1, column=1, pady=5, padx=5)

        ctk.CTkLabel(form_frame, text="Рост (см):").grid(
            row=2, column=0, sticky="w", pady=5, padx=5
        )
        self.ent_height = ctk.CTkEntry(form_frame, width=250)
        self.ent_height.grid(row=2, column=1, pady=5, padx=5)

        ctk.CTkLabel(form_frame, text="Вес (кг):").grid(
            row=3, column=0, sticky="w", pady=5, padx=5
        )
        self.ent_weight = ctk.CTkEntry(form_frame, width=250)
        self.ent_weight.grid(row=3, column=1, pady=5, padx=5)

        ctk.CTkLabel(form_frame, text="Языки (через запятую):").grid(
            row=4, column=0, sticky="w", pady=5, padx=5
        )
        self.ent_langs = ctk.CTkEntry(form_frame, width=250)
        self.ent_langs.grid(row=4, column=1, pady=5, padx=5)

        self.switch_car = ctk.CTkSwitch(form_frame, text="Есть автомобиль")
        self.switch_car.grid(row=5, column=1, pady=10, sticky="w")

        btn_frame = ctk.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=20)

        self.btn_add_json = ctk.CTkButton(
            btn_frame,
            text="Добавить в JSON",
            fg_color="#2c3e50",
            command=lambda: self.save_employee(to_json=True),
        )
        self.btn_add_json.pack(side="left", padx=10)

        self.btn_add_csv = ctk.CTkButton(
            btn_frame,
            text="Добавить напрямую в CSV",
            fg_color="#27ae60",
            hover_color="#219653",
            command=lambda: self.save_employee(to_json=False),
        )
        self.btn_add_csv.pack(side="right", padx=10)

        self.lbl_status = ctk.CTkLabel(tab, text="", text_color="green")
        self.lbl_status.pack()

    def setup_tab_analytics(self, tab):
        lang_frame = ctk.CTkFrame(tab)
        lang_frame.pack(fill="x", padx=10, pady=10)

        self.entry_filter_lang = ctk.CTkEntry(
            lang_frame, placeholder_text="Язык программирования (например: C++)"
        )
        self.entry_filter_lang.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        btn_filter_lang = ctk.CTkButton(
            lang_frame, text="Фильтр по языку", command=self.filter_by_language
        )
        btn_filter_lang.pack(side="right", padx=10, pady=10)

        # Блок расчета среднего роста
        year_frame = ctk.CTkFrame(tab)
        year_frame.pack(fill="x", padx=10, pady=10)

        self.entry_filter_year = ctk.CTkEntry(
            year_frame, placeholder_text="Пороговый год рождения (например: 1995)"
        )
        self.entry_filter_year.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        btn_filter_year = ctk.CTkButton(
            year_frame, text="Расчет ср. роста", command=self.average_height_by_year
        )
        btn_filter_year.pack(side="right", padx=10, pady=10)

        self.txt_analytics_output = ctk.CTkTextbox(tab, width=620, height=200)
        self.txt_analytics_output.pack(pady=10)

    def show_log(self, text, target_textbox=None):
        box = target_textbox if target_textbox else self.txt_output
        box.configure(state="normal")
        box.delete("1.0", ctk.END)
        box.insert("1.0", text)
        box.configure(state="disabled")

    def json_to_csv(self):
        data = load_json_data()
        if not data:
            self.show_log("[-] Исходный JSON пуст.")
            return

        fieldnames = list(data.keys())
        with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                row_copy = row.copy()
                if isinstance(row_copy.get("languages"), list):
                    row_copy["languages"] = ", ".join(row_copy["languages"])
                writer.writerow(row_copy)

        self.show_log(f"[+] База успешно синхронизирована с файлом {CSV_FILE}")

    def find_employee(self):
        data = load_json_data()
        search_query = self.entry_search_name.get().strip().lower()

        results = []
        for emp in data:
            if not search_query or search_query in emp.get("name", "").lower():
                emp_info = (
                    f"Имя: {emp.get('name')}\n"
                    f"Дата рождения: {emp.get('birthday')}\n"
                    f"Рост: {emp.get('height')} см | Вес: {emp.get('weight')} кг\n"
                    f"Автомобиль: {'Да' if emp.get('car') else 'Нет'}\n"
                    f"Языки: {', '.join(emp.get('languages', []))}\n"
                    f"{'-'*40}\n"
                )
                results.append(emp_info)

        if results:
            self.show_log("".join(results))
        else:
            self.show_log("[-] Сотрудники не найдены.")

    def save_employee(self, to_json=True):
        name = self.ent_name.get().strip()
        birthday = self.ent_birth.get().strip()

        try:
            height = int(self.ent_height.get().strip())
            weight = float(self.ent_weight.get().strip())
        except ValueError:
            self.lbl_status.configure(
                text="Ошибка: рост и вес должны быть числами!", text_color="red"
            )
            return

        langs_list = [
            l.strip() for l in self.ent_langs.get().split(",") if l.strip()
        ]
        car = self.switch_car.get() == 1

        if to_json:
            data = load_json_data()
            data.append(
                {
                    "name": name,
                    "birthday": birthday,
                    "height": height,
                    "weight": weight,
                    "car": car,
                    "languages": langs_list,
                }
            )
            with open(JSON_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            self.lbl_status.configure(
                text="[+] Успешно сохранено в JSON!", text_color="green"
            )
        else:
            fieldnames = ["name", "birthday", "height", "weight", "car", "languages"]
            file_exists = os.path.exists(CSV_FILE)
            with open(CSV_FILE, "a", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(
                    {
                        "name": name,
                        "birthday": birthday,
                        "height": height,
                        "weight": weight,
                        "car": str(car),
                        "languages": ", ".join(langs_list),
                    }
                )
            self.lbl_status.configure(
                text="[+] Успешно записано в CSV напрямую!", text_color="green"
            )

        for entry in [
            self.ent_name,
            self.ent_birth,
            self.ent_height,
            self.ent_weight,
            self.ent_langs,
        ]:
            entry.delete(0, ctk.END)
        self.switch_car.deselect()

    def filter_by_language(self):
        data = load_json_data()
        search_lang = self.entry_filter_lang.get().strip().lower()

        if not search_lang:
            self.show_log(
                "[-] Введите язык программирования.", self.txt_analytics_output
            )
            return

        results = [f"Сотрудники со знанием {search_lang.upper()}:\n"]
        for emp in data:
            langs = [str(lang).lower() for lang in emp.get("languages", [])]
            if search_lang in langs:
                results.append(
                    f"- {emp.get('name')} [{', '.join(emp.get('languages'))}]\n"
                )

        if len(results) > 1:
            self.show_log("".join(results), self.txt_analytics_output)
        else:
            self.show_log(
                "[-] Ни один сотрудник не найден.", self.txt_analytics_output
            )

    def average_height_by_year(self):
        data = load_json_data()
        try:
            target_year = int(self.entry_filter_year.get().strip())
        except ValueError:
            self.show_log(
                "[-] Введите корректный год (число).", self.txt_analytics_output
            )
            return

        heights = []
        for emp in data:
            birthday = emp.get("birthday", "")
            try:
                emp_year = int(birthday.split(".")[-1])
                if emp_year < target_year:
                    heights.append(emp.get("height", 0))
            except (ValueError, IndexError):
                continue

        if heights:
            avg_height = sum(heights) / len(heights)
            self.show_log(
                f"Результат расчета:\n\n[+] Средний рост сотрудников, "
                f"родившихся до {target_year} года: {avg_height:.2f} см",
                self.txt_analytics_output,
            )
        else:
            self.show_log(
                f"[-] Нет сотрудников, родившихся до {target_year} года.",
                self.txt_analytics_output,
            )


if __name__ == "__main__":
    app = EmployeeApp()
    app.mainloop()
