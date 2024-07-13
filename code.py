from tkinter import *
import sqlite3
root = Tk()
root.geometry("500x500")

root.title("A player contribution simulator")


home_page = Frame(root)
sign_up_page = Frame(root)
sign_up_page_2 = Frame(root)
login_page = Frame(root)
start_page = Frame(root)

frames = [home_page, sign_up_page, sign_up_page_2, login_page, start_page]

for page in frames:
    page.grid(row=0, column=0, sticky="nsew")

def home_page_create():
    lbl_1 = Label(home_page, text="This is the home page")
    lbl_1.grid(row=0, column=0, pady=20)

    login_btn = Button(home_page, text='Login', command=lambda: login_page.tkraise())
    login_btn.grid(row=1, column=0, ipadx=5, ipady=10)

    sign_up_btn = Button(home_page, text='Sign up', command=lambda: sign_up_page.tkraise())
    sign_up_btn.grid(row=2, column=0, ipadx=5, ipady=10)

    menu_btn = Button(home_page, text='Menu')
    menu_btn.grid(row=3, column=0, ipadx=5, ipady=10)

def sign_up_page_create():
    lbl_2 = Label(sign_up_page, text="This is sign up page 1")
    lbl_2.grid(row=0, column=1, pady=10)

    email_lbl = Label(sign_up_page, text="Email address")
    email_lbl.grid(row=1, column=1, pady=10)

    email_entry = Entry(sign_up_page, width = 10)
    email_entry.grid(row=2, column=1, pady=10)

    first_name_lbl = Label(sign_up_page, text="First name")
    first_name_lbl.grid(row=3, column=1, pady=10)

    first_name_entry = Entry(sign_up_page, width = 10)
    first_name_entry.grid(row=4, column=1, pady=10)

    last_name_lbl = Label(sign_up_page, text="Last name")
    last_name_lbl.grid(row=5, column=1, pady=10)

    last_name_entry = Entry(sign_up_page, width = 10)
    last_name_entry.grid(row=6, column=1, pady=10)

    date_lbl = Label(sign_up_page, text="Date")
    date_lbl.grid(row=7, column=1, pady=10)

    date_scale_month = Scale(sign_up_page, from_= 1, to = 12, orient = HORIZONTAL)
    date_scale_month.grid(row=8, column=1, pady=10)

    date_scale_month = Scale(sign_up_page, from_=1, to= 31, orient = HORIZONTAL)
    date_scale_month.grid(row=9, column=1, pady=10)

    date_scale_month = Scale(sign_up_page, from_=1920, to= 2020, orient = HORIZONTAL)
    date_scale_month.grid(row=10, column=1, pady=10)

    back_btn = Button(sign_up_page, text='Back', command=lambda: home_page.tkraise())
    back_btn.grid(row=11, column=0, ipadx=5, ipady=10)

    next_btn = Button(sign_up_page, text='Next', command=lambda: sign_up_page_2.tkraise())
    next_btn.grid(row=11, column=2, ipadx=5, ipady=10)


def sign_up_page_2_create():
    lbl_3 = Label(sign_up_page_2, text="This is the sign up page 2")
    lbl_3.grid(row=0, column=1, pady=10)

    username_lbl = Label(sign_up_page_2, text="Username")
    username_lbl.grid(row=1, column=1, pady=10)

    username_entry = Entry(sign_up_page_2, width=10)
    username_entry.grid(row=2, column=1, pady=10)

    password_lbl = Label(sign_up_page_2, text="Password")
    password_lbl.grid(row=3, column=1, pady=10)

    password_entry = Entry(sign_up_page_2, width=10)
    password_entry.grid(row=4, column=1, pady=10)

    password_confirmation_lbl = Label(sign_up_page_2, text="Password confirmation")
    password_confirmation_lbl.grid(row=5, column=1, pady=10)

    password_confirmation_entry = Entry(sign_up_page_2, width=10)
    password_confirmation_entry.grid(row=6, column=1, pady=10)

    back_btn = Button(sign_up_page_2, text='Back', command=lambda: sign_up_page.tkraise())
    back_btn.grid(row=7, column=0, ipadx=5, ipady=10)

    next_btn = Button(sign_up_page_2, text='Next', command=lambda: login_page.tkraise())
    next_btn.grid(row=7, column=2, ipadx=5, ipady=10)

def login_create():
    lbl_4 = Label(login_page, text="This is the login page")
    lbl_4.grid(row=0, column=1, pady=10)

    email_or_username_lbl = Label(login_page, text="Email or username")
    email_or_username_lbl.grid(row=1, column=1, pady=10)

    email_or_username_entry = Entry(login_page, width=10)
    email_or_username_entry.grid(row=2, column=1, pady=10)

    password_lbl = Label(login_page, text="Password")
    password_lbl.grid(row=3, column=1, pady=10)

    password_entry = Entry(login_page, width=10)
    password_entry.grid(row=4, column=1, pady=10)

    back_btn = Button(login_page, text='Back', command=lambda: home_page.tkraise())
    back_btn.grid(row=5, column=0, ipadx=5, ipady=10)

    next_btn = Button(login_page, text='Next', command=lambda: start_page.tkraise())
    next_btn.grid(row=5, column=2, ipadx=10, ipady=10)

home_page_create()
sign_up_page_create()
sign_up_page_2_create()
login_create()

home_page.tkraise()
root.mainloop()