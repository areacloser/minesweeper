import os
from tkinter import *
from random import randint
from tkinter.messagebox import *

if os.path.exists("config/config.ini"):
    with open("config/config.ini", "r", encoding="utf-8") as file:
        ls = file.readlines()
        height = int(ls[1].strip("\n"))
        width = int(ls[3].strip("\n"))
        minec = int(ls[5].strip("\n"))
else:
    width = 20
    height = 20
    minec = 50

flagc = 0
time = 0
overed = 0

minepos = []
flagpos = []

exp = 0
mp = [[0 for _ in range(width)] for _ in range(height)]
smp = [[0 for _ in range(width)] for _ in range(height)]
fmp = [[0 for _ in range(width)] for _ in range(height)]

while exp < minec:
    a, b = randint(0, height-1), randint(0, width-1)
    if mp[a][b] == 0:
        mp[a][b] = -1
        minepos.append([a, b])
        exp += 1

for i, j in minepos:
    for a in range(i-1, i+2):
        for b in range(j-1,j+2):
            if a >= 0 and a < height and b >= 0 and b < width:
                if mp[a][b] != -1:
                    mp[a][b] += 1        

"""
for i in mp:
    for j in i:
        print(j,end="\t")
    print("\n\n")
"""

win = Tk()
win.resizable(0, 0)
win.geometry("+200+200")
win.title("扫雷 V1.2.6 -- By lanlan2_")
win.iconbitmap("images/icon.ico")
win.config(bg="aliceblue")

img = PhotoImage(file="images/mine.png")
img2 = PhotoImage(file="images/flag.png")

can = Canvas(win,
             height=height*20+1,
             width=width*20+1,
             borderwidth=0,
             highlightthickness=0,
             relief=FLAT,
             bg="lightgrey")

for i in range(height):
    for j in range(width):
        can.create_rectangle(j*20, i*20, j*20+20, i*20+20, fill="lightblue", outline="blue")

can.pack()

fm = Frame(win, bg="aliceblue")
fm.pack(expand=True, fill=BOTH)
lab_time = Label(fm, text="用时"+str(time)+"秒", bg="aliceblue", font="curier 10")
lab_time.pack(side=LEFT)
lab_mine = Label(fm, text="还剩"+str(minec)+"颗雷", bg="aliceblue", font="curier 10")
lab_mine.pack(side=RIGHT)

def settext(m,n):
    if mp[m][n] == 1:
        color = "Blue"
    elif mp[m][n] == 2:
        color = "Green"
    elif mp[m][n] == 3:
        color = "Red"
    elif mp[m][n] == 4:
        color = "DarkBlue"
    elif mp[m][n] == 5:
        color = "DarkRed"
    elif mp[m][n] == 6:
        color = "DarkGreen"
    elif mp[m][n] == 7:
        color = "Violet"
    else:
        color = "DarkViolet"
    can.create_text(n*20+10, m*20+10, text=mp[m][n], font="consolas 12 bold", fill=color)
    

def visit(m,n):
    if mp[m][n] == 0:
        smp[m][n] = 1
        mp[m][n] = 9
        can.create_rectangle(n*20, m*20, n*20+20, m*20+20, fill="aliceblue", outline="Blue")
        if m+1 >= 0 and m+1 < height and mp[m+1][n] == 0 and fmp[m+1][n] == 0:
            visit(m+1, n)
		    
        if m-1 >= 0 and m-1 < height and mp[m-1][n] == 0 and fmp[m-1][n] == 0:
            visit(m-1, n)
            		    
        if n+1 >= 0 and n+1 < width and mp[m][n+1] == 0 and fmp[m][n+1] == 0:
            visit(m, n+1)
		    
        if n-1 >= 0 and n-1 < width and mp[m][n-1] == 0 and fmp[m][n-1] == 0:
            visit(m, n-1)
            
        if m+1 >= 0 and m+1 < height and n+1 >= 0 and n+1 < width and mp[m+1][n+1] != 9 and mp[m+1][n+1] != 0 and fmp[m+1][n+1] == 0:
            can.create_rectangle((n+1)*20, (m+1)*20, (n+1)*20+20, (m+1)*20+20, fill="aliceblue", outline="blue")
            settext(m+1, n+1)
            smp[m+1][n+1] = 1
                    
        if m-1 >= 0 and m-1 < height and n-1 >= 0 and n-1 < width and mp[m-1][n-1] != 9 and mp[m-1][n-1] != 0 and fmp[m-1][n-1] == 0:
            can.create_rectangle((n-1)*20, (m-1)*20, (n-1)*20+20, (m-1)*20+20, fill="aliceblue", outline="blue")
            settext(m-1, n-1)
            smp[m-1][n-1] = 1
                    
        if m+1 >= 0 and m+1 < height and n-1 >= 0 and n-1 < width and mp[m+1][n-1] != 9 and mp[m+1][n-1] != 0 and fmp[m+1][n-1] == 0:
            can.create_rectangle((n-1)*20, (m+1)*20, (n-1)*20+20, (m+1)*20+20, fill="aliceblue", outline="blue")
            settext(m+1, n-1)
            smp[m+1][n-1] = 1
                    
        if m-1 >= 0 and m-1 < height and n+1 >= 0 and n+1 < width and mp[m-1][n+1] != 9 and mp[m-1][n+1] != 0 and fmp[m-1][n+1] == 0:
            can.create_rectangle((n+1)*20, (m-1)*20, (n+1)*20+20, (m-1)*20+20, fill="aliceblue", outline="blue")
            settext(m-1, n+1)
            smp[m-1][n+1] = 1

        if m+1 >= 0 and m+1 < height and mp[m+1][n] != 9 and fmp[m+1][n] == 0:
            can.create_rectangle(n*20, (m+1)*20, n*20+20, (m+1)*20+20, fill="aliceblue", outline="blue")
            settext(m+1, n)
            smp[m+1][n] = 1
                    
        if m-1 >= 0 and m-1 < height and mp[m-1][n] != 9 and fmp[m-1][n] == 0:
            can.create_rectangle(n*20, (m-1)*20, n*20+20, (m-1)*20+20, fill="aliceblue", outline="blue")
            settext(m-1, n)
            smp[m-1][n] = 1
                    
        if n-1 >= 0 and n-1 < width and mp[m][n-1] != 9 and fmp[m][n-1] == 0:
            can.create_rectangle((n-1)*20, m*20, (n-1)*20+20, m*20+20, fill="aliceblue", outline="blue")
            settext(m, n-1)
            smp[m][n-1] = 1
                    
        if n+1 >= 0 and n+1 < width and mp[m][n+1] != 9 and fmp[m][n+1] == 0:
            can.create_rectangle((n+1)*20, m*20, (n+1)*20+20, m*20+20, fill="aliceblue", outline="blue")
            settext(m, n+1)
            smp[m][n+1] = 1

def over():
    global img, overed
    overed = 1
    for i, j in flagpos:
        if mp[i][j] != -1:
            can.create_line(j*20+3, i*20+3, j*20+20-3, i*20+20-3, fill="red", capstyle=ROUND, width=2)
            can.create_line(j*20+20-3, i*20+3, j*20+3, i*20+20-3, fill="red", capstyle=ROUND, width=2)
    for i, j in minepos:
        can.create_image(j*20+10, i*20+10, image=img)
    
def uncover(event):
    global time
    uncovered = 0
    if event.x >= width*20 or event.y >= height*20:
        return
    x = int(event.x // 20)
    y = int(event.y // 20)
    if fmp[y][x] == 1:
        return
    can.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill="aliceblue", outline="blue")
    if mp[y][x] == 0:
        visit(y, x)
    else:
        if mp[y][x] != 9:
            if mp[y][x] != -1:
                settext(y, x)
                smp[y][x] = 1
            else:
                can.unbind("<Button-1>")
                can.unbind("<Button-3>")
                over()
                showinfo("提示", "您踩到地雷了！")
            
    for i in smp:
        uncovered += i.count(0)
    if uncovered == minec:
        can.unbind("<Button-1>")
        can.unbind("<Button-3>")
        over()
        showinfo("提示", "您成功扫除了所有的雷！用时%d秒" %(time-1))

def setflag(event):
    global minec, flagc
    if event.x >= width*20 or event.y >= height*20:
        return
    x = int(event.x // 20)
    y = int(event.y // 20)
    if fmp[y][x] == 0 and smp[y][x] == 0:
        fmp[y][x] = 1
        flagpos.append([y,x])
        flagc += 1
        lab_mine["text"] = "还剩"+str(minec-flagc)+"颗雷"
        can.create_image(x*20+10, y*20+10, image=img2)
    else:
        fmp[y][x] = 0
        if smp[y][x] == 0:
            flagpos.remove([y,x])
            flagc -= 1
            lab_mine["text"] = "还剩"+str(minec-flagc)+"颗雷"
            can.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill="lightblue", outline="blue")
        
def counttime():
    global time, overed
    if overed == 1:
        return
    lab_time["text"] = "用时"+str(time)+"秒"
    time += 1
    win.after(1000, counttime)

counttime()

can.bind("<Button-1>", uncover)
can.bind("<Button-3>", setflag)
win.mainloop()
