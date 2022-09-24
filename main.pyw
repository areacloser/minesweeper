from tkinter import *
from random import randint
from tkinter.messagebox import *

width = 20
height = 20
minec = 10

minepos = []

exp = 0
mp = [[0 for _ in range(width)] for _ in range(height)]
smp = [[0 for _ in range(width)] for _ in range(height)]

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
win.title("扫雷 V1.0.3 -- By lanlan2_")
win.iconbitmap("icon.ico")
win.config(bg="aliceblue")

img = PhotoImage(file="mine.png")

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

def visit(m,n):
    if mp[m][n] == 0:
        smp[m][n] = 1
        mp[m][n] = 9
        can.create_rectangle(n*20, m*20, n*20+20, m*20+20, fill="aliceblue", outline="blue")
        if m+1 >= 0 and m+1 < height and mp[m+1][n] == 0:
            visit(m+1, n)
		    
        if m-1 >= 0 and m-1 < height and mp[m-1][n] == 0:
            visit(m-1, n)
            		    
        if n+1 >= 0 and n+1 < width and mp[m][n+1] == 0:
            visit(m, n+1)
		    
        if n-1 >= 0 and n-1 < width and mp[m][n-1] == 0:
            visit(m, n-1)
            
        if m+1 >= 0 and m+1 < height and n+1 >= 0 and n+1 < width and mp[m+1][n+1] != 9 and mp[m+1][n+1] != 0:
            can.create_rectangle((n+1)*20, (m+1)*20, (n+1)*20+20, (m+1)*20+20, fill="aliceblue", outline="blue")
            can.create_text((n+1)*20+10, (m+1)*20+10, text=mp[m+1][n+1])
            smp[m+1][n+1] = 1
                    
        if m-1 >= 0 and m-1 < height and n-1 >= 0 and n-1 < width and mp[m-1][n-1] != 9 and mp[m-1][n-1] != 0:
            can.create_rectangle((n-1)*20, (m-1)*20, (n-1)*20+20, (m-1)*20+20, fill="aliceblue", outline="blue")
            can.create_text((n-1)*20+10, (m-1)*20+10, text=mp[m-1][n-1])
            smp[m-1][n-1] = 1
                    
        if m+1 >= 0 and m+1 < height and n-1 >= 0 and n-1 < width and mp[m+1][n-1] != 9 and mp[m+1][n-1] != 0:
            can.create_rectangle((n-1)*20, (m+1)*20, (n-1)*20+20, (m+1)*20+20, fill="aliceblue", outline="blue")
            can.create_text((n-1)*20+10, (m+1)*20+10, text=mp[m+1][n-1])
            smp[m+1][n-1] = 1
                    
        if m-1 >= 0 and m-1 < height and n+1 >= 0 and n+1 < width and mp[m-1][n+1] != 9 and mp[m-1][n+1] != 0:
            can.create_rectangle((n+1)*20, (m-1)*20, (n+1)*20+20, (m-1)*20+20, fill="aliceblue", outline="blue")
            can.create_text((n+1)*20+10, (m-1)*20+10, text=mp[m-1][n+1])
            smp[m-1][n+1] = 1

        if m+1 >= 0 and m+1 < height and mp[m+1][n] != 9:
            can.create_rectangle(n*20, (m+1)*20, n*20+20, (m+1)*20+20, fill="aliceblue", outline="blue")
            can.create_text(n*20+10, (m+1)*20+10, text=mp[m+1][n])
            smp[m+1][n] = 1
                    
        if m-1 >= 0 and m-1 < height and mp[m-1][n] != 9:
            can.create_rectangle(n*20, (m-1)*20, n*20+20, (m-1)*20+20, fill="aliceblue", outline="blue")
            can.create_text(n*20+10, (m-1)*20+10, text=mp[m-1][n])
            smp[m-1][n] = 1
                    
        if n-1 >= 0 and n-1 < width and mp[m][n-1] != 9:
            can.create_rectangle((n-1)*20, m*20, (n-1)*20+20, m*20+20, fill="aliceblue", outline="blue")
            can.create_text((n-1)*20+10, m*20+10, text=mp[m][n-1])
            smp[m][n-1] = 1
                    
        if n+1 >= 0 and n+1 < width and mp[m][n+1] != 9:
            can.create_rectangle((n+1)*20, m*20, (n+1)*20+20, m*20+20, fill="aliceblue", outline="blue")
            can.create_text((n+1)*20+10, m*20+10, text=mp[m][n+1])
            smp[m][n+1] = 1

def over():
    global img
    for i, j in minepos:
        can.create_image(j*20+10, i*20+10, image=img)
    
def uncover(event):
    uncovered = 0
    if event.x >= width*20 or event.y >= height*20:
        return
    x = int(event.x // 20)
    y = int(event.y // 20)
    can.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill="aliceblue", outline="blue")
    if mp[y][x] == 0:
        visit(y, x)
    else:
        if mp[y][x] != 9:
            if mp[y][x] != -1:
                can.create_text(x*20+10, y*20+10, text=mp[y][x])
                smp[y][x] = 1
            else:
                can.unbind("<Button-1>")
                over()
                showinfo("提示", "您踩到地雷了！")
            
    for i in smp:
        uncovered += i.count(0)
    if uncovered == minec:
        can.unbind("<Button-1>")
        over()
        showinfo("提示", "您成功扫除了所有的雷！")

can.bind("<Button-1>", uncover)
win.mainloop()
