#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 上午11:29
# @Author  : tangming
# @File    : Scale.py

from tkinter import *

win = Tk()
win.title("My Windows")
win.geometry("200x200")

l = Label(win, bg="green", width=20, text="empty")
l.pack()


def print_selection(v):
    l.config(text="You have selected " + v)


s = Scale(win, label="try me", from_=5, to_=11, orient=HORIZONTAL,
          length=200, showvalue=0, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()

win.mainloop()