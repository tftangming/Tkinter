#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19-8-4 下午4:51
# @Author  : tangming
# @File    : load_windows03.py


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
    window_sign_up = Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("Sign up window")

    def sign_to_My_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()  # 如果换成quit()会导致主窗口也关闭

    new_name = StringVar()
    new_name.set('example@python.com')
    Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = StringVar()
    Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = StringVar()
    Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = Button(window_sign_up, text='Sign up', command=sign_to_My_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()