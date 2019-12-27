#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午12:02
# @Author  : tangming
# @File    : Canvas.py

from tkinter import *

win = Tk()
win.title("Canvas-Use")
win.geometry("200x200")

canvas = Canvas(win, bg="blue", height=100, width=200)
# 加载图片放在画布上
image_file = PhotoImage(file="ins.gif")
image = canvas.create_image(10, 10, anchor="nw", image=image_file)
# 在画布上画线/圆/矩形
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(0,0,20,20,fill="red")
rect = canvas.create_rectangle(100,30,100+20,30+20)
canvas.pack()


def moveit():
    canvas.move(rect, 0, 2)


b = Button(win, text="move", command=moveit).pack()
win.mainloop()