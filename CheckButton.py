#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 上午11:40
# @Author  : tangming
# @File    : CheckButton.py

# 勾选项
from tkinter import *

win = Tk()
win.title("CheckButton-Use")
win.geometry("200x200")

var = StringVar()

l = Label(win, bg="green", width=20, text="empty")
l.pack()


def print_selection():
    if (var1.get() == 1) and (var2.get() == 0):
        l.config(text="I love only Python")
    elif (var1.get() == 0) and (var2.get() == 1):
        l.config(text="I love only C++")
    elif (var1.get() == 0) and (var2.get() == 0):
        l.config(text="I do not love either")
    else:
        l.config(text="I love both")


var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(win, text="Python", variable=var1, onvalue=1, offvalue=0,
                 command=print_selection)
c2 = Checkbutton(win, text="C++",  variable=var2, onvalue=1, offvalue=0,
                 command=print_selection)
c1.pack()
c2.pack()
win.mainloop()