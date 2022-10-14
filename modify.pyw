import os
from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.resizable(0, 0)
win.geometry("+200+200")
win.title("设置")
win.iconbitmap("images/icon.ico")

fm1 = Frame(win)
fm1.pack(pady=10)
fm2 = Frame(win)
fm2.pack(fill=BOTH, pady=10)

height = IntVar()
width = IntVar()
minec = IntVar()
ls = []

if os.path.exists("config/config.ini"):
    with open("config/config.ini", "r", encoding="utf-8") as file:
        ls = file.readlines()
        height.set(int(ls[1].strip("\n")))
        width.set(int(ls[3].strip("\n")))
        minec.set(int(ls[5].strip("\n")))
else:
    height.set(20)
    width.set(20)
    minec.set(20)

lab1 = Label(fm1, text="宽度:", font="黑体 20 bold", fg="red")
lab1.grid(row=0, column=0)
spin1 = Spinbox(fm1,
                borderwidth=1,
                font="System 25 bold",
                fg="red",
                from_=1,
                to = 40,
                increment=1,
                width=10,
                textvariable=height)
spin1.grid(row=0, column=1)

lab2 = Label(fm1, text="长度:", font="黑体 20 bold", fg="green")
lab2.grid(row=1, column=0)
spin2 = Spinbox(fm1,
                borderwidth=1,
                font="System 25 bold",
                fg="green",
                from_=1,
                to = 40,
                increment=1,
                width=10,
                textvariable=width)
spin2.grid(row=1, column=1)

lab3 = Label(fm1, text="雷数:", font="黑体 20 bold", fg="blue")
lab3.grid(row=2, column=0)
spin3 = Spinbox(fm1,
                borderwidth=1,
                font="System 25 bold",
                fg="blue",
                from_=1,
                to = 40,
                increment=1,
                width=10,
                textvariable=minec)
spin3.grid(row=2, column=1)

def submit():
    global ls
    if height.get() * width.get() <= minec.get() - 1:
        showwarning("警告", "地雷数过大！")
    elif height.get() > 40:
        showwarning("警告", "宽度过大！")
    elif width.get() > 40:
        showwarning("警告", "长度过大！")
    else:
        if not os.path.exists("config/config.ini"):
            showwarning("警告", "不存在config.ini配置文件！")
        else:
            with open("config/config.ini", "w") as file:
                for i in range(6):
                    if i == 1:
                        file.write(str(height.get())+"\n")
                    elif i == 3:
                        file.write(str(width.get())+"\n")
                    elif i == 5:
                        file.write(str(minec.get())+"\n")
                    else:
                        file.write(ls[i])
            showinfo("提示", "设置成功！")
    
but1 = Button(fm2, text="确定", relief=GROOVE, font="黑体 20 bold", command=submit)
but1.pack(side=LEFT, ipadx=10, padx=20)

but2 = Button(fm2, text="退出", relief=GROOVE, font="黑体 20 bold", command=win.destroy)
but2.pack(side=RIGHT, ipadx=10, padx=20)
win.mainloop()
