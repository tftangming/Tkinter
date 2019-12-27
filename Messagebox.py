#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午1:53
# @Author  : tangming
# @File    : Messagebox.py

# 使用框架/容器
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Frame-Use")
win.geometry("300x300")

#　创建消息窗口
def hit_me():
    # messagebox.showinfo(title="Hi", message="hahahaha")
    # messagebox.showwarning(title="Hi",message="nononono")
    # messagebox.showerror(title="Hi", message="No!!never")
    # print messagebox.askquestion(title="Hi", message="hahaha")  # return "res", "no"
    # print messagebox.askyesno(title="Hi", message="hahaha")      # return True, False
    print messagebox.askretrycancel(title="Hi", message="hahaha")

b1 = Button(win,text="hit me", command=hit_me)
b1.pack()


win.mainloop()