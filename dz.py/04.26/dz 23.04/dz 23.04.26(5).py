import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class CESAR(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("CESAR")
        self.geometry("500x550")

        self.label_msg = ctk.CTkLabel(self, text="Сообщение:")
        self.label_msg.pack(pady=(20, 0))

        self.entry_text = ctk.CTkTextbox(self, height=100, width=400)
        self.entry_text.pack(pady=10)

        self.label_shift = ctk.CTkLabel(self, text="Сдвиг:")
        self.label_shift.pack()

        self.entry_shift = ctk.CTkEntry(self, width=100)
        self.entry_shift.insert(0, "3")
        self.entry_shift.pack(pady=10)

        self.btn_encrypt = ctk.CTkButton(self, text="Зашифровать", command=self.handle_encrypt)
        self.btn_encrypt.pack(pady=5)

        self.btn_decrypt = ctk.CTkButton(self, text="Дешифровать", command=self.handle_decrypt)
        self.btn_decrypt.pack(pady=5)
        
        self.btn_brute = ctk.CTkButton(self, text="Взломать", fg_color="transparent", border_width=2, command=self.handle_brute)
        self.btn_brute.pack(pady=10)

        self.label_res = ctk.CTkLabel(self, text="Результат")
        self.label_res.pack(pady=(10, 0))

        self.result_text = ctk.CTkTextbox(self, height=150, width=400)
        self.result_text.pack(pady=10)

    def pro_text(self, text, shift):
        result = ""
        ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        en_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
        for char in text:
            lower_char = char.lower()
            if lower_char in ru_alphabet:
                idx = (ru_alphabet.find(lower_char) + shift) % 33
                new_char = ru_alphabet[idx]
                result += new_char.upper() if char.isupper() else new_char
            elif lower_char in en_alphabet:
                idx = (en_alphabet.find(lower_char) + shift) % 26
                new_char = en_alphabet[idx]
                result += new_char.upper() if char.isupper() else new_char
            else:
                result += char
        return result

    def handle_encrypt(self):
        text = self.entry_text.get("1.0", "end-1c")
        try:
            shift = int(self.entry_shift.get())
            res = self.pro_text(text, shift)
            self.update_result(res)
        except ValueError:
            self.update_result("Ошибка: введите целое число!")

    def handle_decrypt(self):
        text = self.entry_text.get("1.0", "end-1c")
        try:
            shift = int(self.entry_shift.get())
            res = self.pro_text(text, -shift)
            self.update_result(res)
        except ValueError:
            self.update_result("Ошибка: введите целое число!")

    def handle_brute(self):
        text = self.entry_text.get("1.0", "end-1c")
        if not text.strip():
            self.update_result("Ошибка: введите текст для взлома")
            return
            
        all_variants = ""
        for s in range(1, 34):
            variant = self.pro_text(text, -s) 
            all_variants += f"Сдвиг {s}: {variant[:50]}...\n" 
        self.update_result(all_variants)

    def update_result(self, text):
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", text)
                                
if __name__ == "__main__":
    app = CESAR()
    app.mainloop()
