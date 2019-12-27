#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午1:43
# @Author  : tangming
# @File    : frame.py

# 使用框架/容器
from tkinter import *

win = Tk()
win.title("Frame-Use")
win.geometry("300x300")

l = Label(win, text="On the windows", bg="yellow")
l.pack()

frame = Frame(win)
frame.pack()
frame_l = Frame(frame)
frame_r = Frame(frame)
frame_l.pack(side="left")
frame_r.pack(side="right")

l1 = Label(frame_l,text="On the frame_l1").pack()
l2 = Label(frame_l,text="On the frame_l2").pack()
l3 = Label(frame_r,text="On the frame_r1").pack()

win.mainloop()