from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import hashlib
import uuid


def func_input1():
    global hashPass
    global c
    c = uuid.uuid1().bytes
    hashPass = hashlib.sha256(c + authorization.get().encode()).hexdigest()

def func_input2():
    if hashPass==hashlib.sha256(c + check.get().encode()).hexdigest():
        showinfo(title="Авторизация", message="Вход выполнен успешно!")
    else:
        showerror(title="Ошибка", message="Введен неверный пароль. Попробуйте ещё раз")

root = Tk()

root.title("Ввод и проверка пароля")
root.geometry("400x200+250+50")
root["bg"] = "#d6f9f1"

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

authorization = ttk.Entry()
authorization.grid(row=0, column=0)

check = ttk.Entry()
check.grid(row=1, column=0)

button1 = Button(text="Ввод", command=func_input1)
button1.grid(row=0,column=1)
button2 = Button(text="Проверить", command=func_input2)
button2.grid(row=1,column=1)


root.mainloop()
