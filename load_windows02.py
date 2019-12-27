#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午4:39
# @Author  : tangming
# @File    : load_windows02.py


from tkinter import *
from tkinter import messagebox
import pickle

window = Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = Canvas(window, height=200, width=500)
image_file = PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
Label(window, text='User name: ').place(x=50, y= 150)
Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = StringVar()
entry_usr_pwd = Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        # 尝试读取这个文件，如果法线找不到该文件，那么就直接创建该文件
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except IOError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = messagebox.askyesno('Welcome',
                               'You have not sign up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()
def usr_sign_up():
    pass

# login and sign up button
btn_login = Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()



