import tkinter as tk
import random
from math import log
from tkinter import messagebox

global button

global list1
list1 = ['snow', 'blanched almond', 'peach puff',
         'khaki1', 'tan1', 'orange2', 'DarkOrange1', 'tomato2']


def change(i, j):
    global button, mat, list1
    mat[i][j] = 2
    button[i][j] = tk.Button(root, text=f'   {mat[i][j]}   ', padx=30, pady=20, bg=list1[1]).grid(
        row=i, column=j, ipady=10, columnspan=1)


def checking():
    global mat
    count = 0
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                count = count + 1
    if(count == 0):
        res = messagebox.askyesno(
            'Game over', f'       You lost the game\nDo you want to play again?')
        if(res):
            for i in range(4):
                for j in range(4):
                    mat[i][j] = 0
            update()
            while(1):
                i, j = random.randint(0, 3), random.randint(0, 3)
                if(mat[i][j] == 0):
                    change(i, j)
                    break

            while(1):
                i, j = random.randint(0, 3), random.randint(0, 3)
                if(mat[i][j] == 0):
                    change(i, j)
                    break

        else:
            root.destroy()


def update():
    global button, mat
    for i in range(4):
        for j in range(4):
            if(mat[i][j] != 0):
                if((len(str(mat[i][j]))) == 1):
                    button[i][j] = tk.Button(root, text=f'   {mat[i][j]}   ', padx=30, pady=20, bg=list1[int(log(mat[i][j], 2))]).grid(
                        row=i, column=j, ipady=10, columnspan=1,)
                elif((len(str(mat[i][j]))) == 2):
                    button[i][j] = tk.Button(root, text=f'  {mat[i][j]}  ', padx=30, pady=20, bg=list1[int(log(mat[i][j], 2))]).grid(
                        row=i, column=j, ipady=10, columnspan=1,)
                elif((len(str(mat[i][j]))) == 3):
                    button[i][j] = tk.Button(root, text=f' {mat[i][j]} ', padx=30, pady=20, bg=list1[int(log(mat[i][j], 2))]).grid(
                        row=i, column=j, ipady=10, columnspan=1,)
                elif((len(str(mat[i][j]))) == 4):
                    button[i][j] = tk.Button(root, text=f'{mat[i][j]}', padx=30, pady=20, bg=list1[int(log(mat[i][j], 2))]).grid(
                        row=i, column=j, ipady=10, columnspan=1,)
            else:
                button[i][j] = tk.Button(root, text="        ", padx=30, pady=20, bg=list1[0]).grid(
                    row=i, column=j, ipady=10, columnspan=1,)
    return


def right():
    global mat
    a = mat
    for i in range(4):
        for j in range(2):
            a[i][j], a[i][3 - j] = a[i][3 - j], a[i][j]

    for i in range(4):
        j = 0
        while(j < 3):
            if(a[i][j] != 0 and j != 3):
                k = j + 1
                p = 0
                while(a[i][k] == 0 and k < 3 and p < 9):
                    a[i].pop(k)
                    a[i].append(0)
                    p = p + 1
                if(a[i][j] == a[i][j + 1]):
                    a[i][j] = a[i][j] + a[i][j]
                    a[i].pop(j + 1)
                    a[i].append(0)
            else:
                if(sum(a[i][j: 4]) != 0):
                    a[i].pop(j)
                    a[i].append(0)
                    j = j - 1

            j = j + 1

    for i in range(4):
        for j in range(2):
            a[i][j], a[i][3 - j] = a[i][3 - j], a[i][j]

    while(1):
        i, j = random.randint(0, 3), random.randint(0, 3)
        if(mat[i][j] == 0):
            change(i, j)
            break
    update()
    checking()
    return


def left():
    global mat
    a = mat
    for i in range(4):
        j = 0
        while(j < 3):

            if(mat[i][j] != 0):
                k = j + 1
                p = 0
                while(mat[i][k] == 0 and k < 3 and p < 6):
                    mat[i].pop(k)
                    mat[i].append(0)
                    p = p + 1
                if(mat[i][j] == mat[i][j + 1]):
                    mat[i][j] = mat[i][j] + mat[i][j]
                    mat[i].pop(k)
                    mat[i].append(0)
            else:
                if(sum(a[i][j: 4]) != 0):
                    a[i].pop(j)
                    a[i].append(0)
                    j = j - 1
            j = j + 1

    while(1):
        i, j = random.randint(0, 3), random.randint(0, 3)
        if(mat[i][j] == 0):
            change(i, j)
            break
    update()
    checking()
    return


def top():
    global mat
    a = mat
    for i in range(4):
        for j in range(i, 4):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    for i in range(4):
        j = 0
        while(j < 3):

            if(mat[i][j] != 0):
                k = j + 1
                p = 0
                while(mat[i][k] == 0 and k < 3 and p < 6):
                    mat[i].pop(k)
                    mat[i].append(0)
                    p = p + 1
                if(mat[i][j] == mat[i][j + 1]):
                    mat[i][j] = mat[i][j] + mat[i][j]
                    mat[i].pop(k)
                    mat[i].append(0)
            else:
                if(sum(a[i][j: 4]) != 0):
                    a[i].pop(j)
                    a[i].append(0)
                    j = j - 1

            j = j + 1

    for i in range(4):
        for j in range(i, 4):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    while(1):
        i, j = random.randint(0, 3), random.randint(0, 3)
        if(mat[i][j] == 0):
            change(i, j)
            break
    update()
    checking()
    return


def bottom():
    global mat
    a = mat
    for i in range(2):
        for j in range(4):
            a[i][j], a[3 - i][j] = a[3 - i][j], a[i][j]

    for i in range(4):
        for j in range(i, 4):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    for i in range(4):
        j = 0
        while(j < 3):

            if(mat[i][j] != 0):
                k = j + 1
                p = 0
                while(mat[i][k] == 0 and k < 3 and p < 6):
                    mat[i].pop(k)
                    mat[i].append(0)
                    p = p + 1
                if(mat[i][j] == mat[i][j + 1]):
                    mat[i][j] = mat[i][j] + mat[i][j]
                    mat[i].pop(k)
                    mat[i].append(0)
            else:
                if(sum(a[i][j: 4]) != 0):
                    a[i].pop(j)
                    a[i].append(0)
                    j = j - 1

            j = j + 1

    for i in range(4):
        for j in range(i, 4):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    for i in range(2):
        for j in range(4):
            a[i][j], a[3 - i][j] = a[3 - i][j], a[i][j]

    while(1):
        i, j = random.randint(0, 3), random.randint(0, 3)
        if(mat[i][j] == 0):
            change(i, j)
            break
    update()
    checking()
    return


root = tk.Tk()
root.title("2048")


button = [[0 for x in range(4)] for x in range(4)]

button[0][0] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=0, column=0, ipady=10)
button[1][0] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=1, column=0, ipady=10)
button[2][0] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=2, column=0, ipady=10)
button[3][0] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=3, column=0, ipady=10)
button[0][1] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=0, column=1, ipady=10)
button[1][1] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=1, column=1, ipady=10)
button[2][1] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=2, column=1, ipady=10)
button[3][1] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=3, column=1, ipady=10)
button[0][2] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=0, column=2, ipady=10)
button[1][2] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=1, column=2, ipady=10)
button[2][2] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=2, column=2, ipady=10)
button[3][2] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=3, column=2, ipady=10)
button[0][3] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=0, column=3, ipady=10)
button[1][3] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=1, column=3, ipady=10)
button[2][3] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=2, column=3, ipady=10)
button[3][3] = tk.Button(root, text="        ", padx=30, pady=20, ).grid(
    row=3, column=3, ipady=10)
button_11 = tk.Button(root, text="", padx=180, pady=5, bg='blue').grid(
    row=4, column=0, ipady=10, columnspan=4)
button_1 = tk.Button(root, text="->", padx=30, pady=10, command=right, bg='pale green').grid(
    row=5, column=0, ipady=10)
button_2 = tk.Button(root, text="<-", padx=30, pady=10, command=left, bg='pale green').grid(
    row=5, column=1, ipady=10)
button_3 = tk.Button(root, text="^", padx=30, pady=10, command=top, bg='pale green').grid(
    row=5, column=2, ipady=10)
button_4 = tk.Button(root, text="v", padx=30, pady=10, command=bottom, bg='pale green').grid(
    row=5, column=3, ipady=10)

global mat
mat = [[0 for i in range(4)]for j in range(4)]
while(1):
    i, j = random.randint(0, 3), random.randint(0, 3)
    if(mat[i][j] == 0):
        change(i, j)
        break

while(1):
    i, j = random.randint(0, 3), random.randint(0, 3)
    if(mat[i][j] == 0):
        change(i, j)
        break


root.mainloop()
