import tkinter as tk
from tkinter import messagebox, font, simpledialog
import random
import string


def generate_password(length):
    # Karakter setlerini tanımla
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Şifreyi oluştur
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Başarılı","Şifre Kopyalandı")

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Hata", "Şifre uzunluğu 1'den büyük olmalıdır.")
            return

        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

def on_generate_again():
    on_generate()

def save_password(name,password):
    if password:
        with open("password.txt", "a") as file:
            file.write(f"{name} ==> {password} \n")
            messagebox.showinfo("Başarılı","Şifre kaydedildi")

def on_save():
    password = entry_password.get()
    if not password:
        messagebox.showerror("Hata","Önce bir sifre oluşturmalısınız.")
        return
    name = simpledialog.askstring("Şifre adı","Şifre adı girin : ")
    if name:
        save_password(name,password)


root = tk.Tk()
root.title("Rastgele Şifre Oluşturucu")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Özel yazı tipi
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=12)

# Şifre uzunluğu etiketi ve girişi
label_length = tk.Label(root, text="Şifre Uzunluğu:", bg="#f0f0f0", font=("Arial", 12))
label_length.pack()

entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack()

# Şifre etiketi ve girişi
label_password = tk.Label(root, text="Oluşturulan Şifre:", bg="#f0f0f0", font=("Arial", 12))
label_password.pack()

entry_password = tk.Entry(root, font=("Arial", 12))
entry_password.pack()

# Şifre oluşturma düğmesi
button_generate = tk.Button(root, text="Şifre Oluştur", command=on_generate, font=("Arial", 12), bg="#4caf50",
                            fg="white", activebackground="#45a049")
button_generate.pack()

button_generate_again = tk.Button(root, text="Tekrar Şifre Oluştur", command=on_generate_again, font=("Arial",12), bg="#FF9800", fg = "white", activebackground="#FB8C00")
button_generate_again.pack()

#Şifre Koplayama Düğmesi
button_copy = tk.Button(root, text="kopyala",command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white", activebackground="#1e88e5")
button_copy.pack()

button_save = tk.Button(root, text="Kaydet", command=on_save, font=("Arial", 12), bg="#0356fc", fg="white",activebackground="#c9bc04")
button_save.pack()

root.mainloop()
