#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午2:09
# @Author  : tangming
# @File    : pack_place_grid.py

# 关于放置的问题
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Frame-Use")
win.geometry("300x300")


Label(win, text="1111111111").place(x=10,y=100, anchor="nw")  #将模块的左上方固定在坐标（10，100）上

win.mainloop()