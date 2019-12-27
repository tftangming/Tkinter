#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 上午11:21
# @Author  : tangming
# @File    : ListButton.py
from tkinter import *

win = Tk()
win.title("LsitButton-Use")
win.geometry("200x200")


l = Label(win, bg="green", width=20, text="empty")
l.pack()


def print_selection():
    l.config(text="You have selected " + var.get())


var = StringVar()
r1 = Radiobutton(win, text="Option A", variable=var, value="A", command=print_selection)
r1.pack()
r2 = Radiobutton(win, text="Option B", variable=var, value="B", command=print_selection)
r2.pack()
r3 = Radiobutton(win, text="Option C", variable=var, value="C", command=print_selection)
r3.pack()

win.mainloop()
