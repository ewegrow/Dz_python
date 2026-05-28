import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class Vigener(ctk.CTk): 
    def __init__(self):
        super().__init__()
        
        self.title("Vigener")
        self.geometry("500x600")

        self.label_msg = ctk.CTkLabel(self, text="Сообщение:")
        self.label_msg.pack(pady=(20, 0))

        self.entry_text = ctk.CTkTextbox(self, height=100, width=400)
        self.entry_text.pack(pady=10)

        self.label_shift = ctk.CTkLabel(self, text="Ключ:")
        self.label_shift.pack()

        self.entry_key = ctk.CTkEntry(self, width=200, placeholder_text="Введите кодовое слово...")
        self.entry_key.pack(pady=10)


        self.btn_encrypt = ctk.CTkButton(self, text="Зашифровать", command=self.handle_encrypt)
        self.btn_encrypt.pack(pady=5)

        self.btn_decrypt = ctk.CTkButton(self, text="Дешифровать", command=self.handle_decrypt)
        self.btn_decrypt.pack(pady=5)
        
        
        self.btn_clear = ctk.CTkButton(self, text="Очистить", fg_color="transparent", border_width=2, command=lambda: self.update_result(""))
        self.btn_clear.pack(pady=10)

        self.label_res = ctk.CTkLabel(self, text="Результат:")
        self.label_res.pack(pady=(10, 0))

        self.result_text = ctk.CTkTextbox(self, height=150, width=400)
        self.result_text.pack(pady=10)

    def vigenere(self, text, key, decrypt=False):
        result = ""
        rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        key = key.lower()
        key_index = 0
        
        for char in text:
            char_lower = char.lower()
            
            if char_lower in rus_alphabet:
                alphabet = rus_alphabet
            elif char_lower in eng_alphabet:
                alphabet = eng_alphabet
            else:
                result += char
                continue
            
            shift_char = key[key_index % len(key)]
            shift = alphabet.index(shift_char) if shift_char in alphabet else 0
            
            if decrypt:
                shift = -shift
                
            idx = (alphabet.index(char_lower) + shift) % len(alphabet)
            new_char = alphabet[idx]
            result += new_char.upper() if char.isupper() else new_char
            
            key_index += 1 
            
        return result

    def handle_encrypt(self):
        text = self.entry_text.get("1.0", "end-1c")
        key = self.entry_key.get()
        if not key:
            self.update_result("Ошибка: введите ключ!")
            return
        res = self.vigenere(text, key)
        self.update_result(res)

    def handle_decrypt(self):
        text = self.entry_text.get("1.0", "end-1c")
        key = self.entry_key.get()
        if not key:
            self.update_result("Ошибка: введите ключ!")
            return
        res = self.vigenere(text, key, decrypt=True)
        self.update_result(res)

    def update_result(self, text):
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", text)
                                
if __name__ == "__main__":
    app = Vigener()
    app.mainloop()
