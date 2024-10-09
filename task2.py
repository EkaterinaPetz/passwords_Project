from tkinter import *
from tkinter.messagebox import showinfo, showerror
import hashlib
import uuid


users = {}
cs = {}

def auth_user():
    login = login_entry.get()

    if login in users:
        showerror(title="Ошибка авторизации", message="Пользователь с таким логином уже существует!")
    else:
        cs[login] = uuid.uuid1().bytes
        users[login] = hashlib.sha256(cs[login] + password_entry.get().encode()).hexdigest()
        showinfo(title="Авторизация", message="Авторизация прошла успешно!")
    login_entry.delete(0, END)
    password_entry.delete(0, END)


def login_user():
    login = login_entry.get()
    password = password_entry.get()

    if login in users and users[login] == hashlib.sha256(cs[login] + password_entry.get().encode()).hexdigest():
        showinfo(title="Вход", message="Вход выполнен успешно!")
    elif login not in users:
        showerror(title="Ошибка входа", message="Пользователь с таким логином не найден!")
    else:
        showerror(title="Ошибка входа", message="Неверный пароль!")


root = Tk()
root.title("Авторизация и вход")
root.geometry("400x200+250+50")
root["bg"] = "#d6f9f1"

login_label = Label(root, text="Логин:", font=("Arial", 12))
login_label.grid(row=0, column=0, padx=10, pady=10)
login_entry = Entry(root, font=("Arial", 12))
login_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = Label(root, text="Пароль:", font=("Arial", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*", font=("Arial", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)

auth_button = Button(root, text="Авторизоваться", command=auth_user, font=("Arial", 12))
auth_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

login_button = Button(root, text="Войти", command=login_user, font=("Arial", 12))
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()