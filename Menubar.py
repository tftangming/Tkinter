#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午12:55
# @Author  : tangming
# @File    : Menubar.py

# 制作菜单
from tkinter import *

win = Tk()
win.title("Menubar-Use")
win.geometry("300x300")

l = Label(win, text="", bg="yellow")
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter +=1


menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=do_job)
filemenu.add_command(label="Open",command=do_job)
filemenu.add_command(label="Save",command=do_job)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=win.quit)


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=do_job)
editmenu.add_command(label="Copy",command=do_job)
editmenu.add_command(label="Paste",command=do_job)

submenu = Menu(filemenu)
filemenu.add_cascade(label="Import",menu=submenu,underline=0)
submenu.add_command(label="Submenu1",command=do_job)

win.config(menu=menubar)


win.mainloop()

