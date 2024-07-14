from tkinter import *
import sqlite3
root = Tk()
root.geometry("400x400")

root.title("A player contribution simulator")

# First database for login details
conn = sqlite3.connect('login.db')

c = conn.cursor()

c.execute("""CREATE TABLE if NOT EXISTS login (
        email_address text,
        first_name text,
        last_name text,
        Date of birth text,
        username text,
        password text
        )""")

conn.commit()

conn.close()

# Second database for 2024 details
conn_1 = sqlite3.connect('2024_stats.db')

c_1 = conn_1.cursor()

c_1.execute("""CREATE TABLE if NOT EXISTS stats_a (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        number_of_days_out_for_injury integer
        )""")

conn_1.commit()

conn_1.close()

# Third database for 2023 details
conn_2 = sqlite3.connect('2023_stats.db')

c_2 = conn_2.cursor()

c_2.execute("""CREATE TABLE if NOT EXISTS stats_b (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        number_of_days_out_for_injury integer
        )""")

conn_2.commit()

conn_2.close()

# Forth database for 2022 details
conn_3 = sqlite3.connect('2022_stats.db')

c_3 = conn_3.cursor()

c_3.execute("""CREATE TABLE if NOT EXISTS stats_c (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        number_of_days_out_for_injury integer
        )""")

conn_3.commit()

conn_3.close()

# Fifth database for 2021 details
conn_4 = sqlite3.connect('2021_stats.db')

c_4 = conn_4.cursor()

c_4.execute("""CREATE TABLE if NOT EXISTS stats_d (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        number_of_days_out_for_injury integer
        )""")

conn_4.commit()

conn_4.close()

# Sixth database for 2020 details
conn_5 = sqlite3.connect('2020_stats.db')

c_5 = conn_5.cursor()

c_5.execute("""CREATE TABLE if NOT EXISTS stats_e (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        number_of_days_out_for_injury integer
        )""")

conn_5.commit()

conn_5.close()

# Seventh database for Munetaka Murakami by team
conn_6 = sqlite3.connect('Munetaka_Murakami_stats_by_team.db')

c_6 = conn_6.cursor()

c_6.execute("""CREATE TABLE if NOT EXISTS Murakami (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_6.commit()

conn_6.close()

# Eighth database for Tetsuto Yamada by team
conn_7 = sqlite3.connect('Tetsuto_Yamada_stats_by_team.db')

c_7 = conn_7.cursor()

c_7.execute("""CREATE TABLE if NOT EXISTS Yamada (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_7.commit()

conn_7.close()

# Database for Domingo Santana by team

conn_8 = sqlite3.connect('Domingo_Santana_stats_by_team.db')

c_8 = conn_8.cursor()

c_8.execute("""CREATE TABLE if NOT EXISTS Santana (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_8.commit()

conn_8.close()

# Database for Jose Osuna by team

conn_9 = sqlite3.connect('Jose_Osuna_stats_by_team.db')

c_9 = conn_9.cursor()

c_9.execute("""CREATE TABLE if NOT EXISTS Osuna (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_9.commit()

conn_9.close()

# Database for Nori Aoki by team

conn_10 = sqlite3.connect('Nori_Aoki_stats_by_team.db')

c_10 = conn_10.cursor()

c_10.execute("""CREATE TABLE if NOT EXISTS Aoki (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_10.commit()

conn_10.close()

# Database for Yasutaka Shiomi by team

conn_11 = sqlite3.connect('Yasutaka_Shiomi_stats_by_team.db')

c_11 = conn_11.cursor()

c_11.execute("""CREATE TABLE if NOT EXISTS Shiomi (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_11.commit()

conn_11.close()

# Database for Yuhei Nakamura by team

conn_12 = sqlite3.connect('Yuhei_Nakamura_stats_by_team.db')

c_12 = conn_12.cursor()

c_12.execute("""CREATE TABLE if NOT EXISTS Nakamura (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_12.commit()

conn_12.close()

# Database for Hideki Nagaoka by team

conn_13 = sqlite3.connect('Hideki_Nagaoka_stats_by_team.db')

c_13 = conn_13.cursor()

c_13.execute("""CREATE TABLE if NOT EXISTS Nagaoka (
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

conn_13.commit()

conn_13.close()


home_page = Frame(root)
sign_up_page = Frame(root)
sign_up_page_2 = Frame(root)
login_page = Frame(root)
start_page = Frame(root)
choosing_player_page = Frame(root)
choosing_year_page = Frame(root)
Menu_page = Frame(root)

frames = [home_page, sign_up_page, sign_up_page_2, login_page, start_page, choosing_player_page, choosing_year_page]

home_page.tkraise()

for page in frames:
    page.grid(row=0, column=0, sticky="nsew")


def home_page_create():
    lbl_1 = Label(home_page, text="This is the home page")
    lbl_1.grid(row=0, column=0, pady=20)

    login_btn = Button(home_page, text='Login', command=lambda: login_page.tkraise())
    login_btn.grid(row=1, column=0, ipadx=5, ipady=10)

    sign_up_btn = Button(home_page, text='Sign up', command=lambda: sign_up_page.tkraise())
    sign_up_btn.grid(row=2, column=0, ipadx=5, ipady=10)


def sign_up_page_create():
    lbl_2 = Label(sign_up_page, text="This is sign up page 1")
    lbl_2.grid(row=0, column=1, pady=10)

    email_lbl = Label(sign_up_page, text="Email address")
    email_lbl.grid(row=1, column=1, pady=10)

    email_entry = Entry(sign_up_page, width=10)
    email_entry.grid(row=2, column=1, pady=10)

    first_name_lbl = Label(sign_up_page, text="First name")
    first_name_lbl.grid(row=3, column=1, pady=10)

    first_name_entry = Entry(sign_up_page, width=10)
    first_name_entry.grid(row=4, column=1, pady=10)

    last_name_lbl = Label(sign_up_page, text="Last name")
    last_name_lbl.grid(row=5, column=1, pady=10)

    last_name_entry = Entry(sign_up_page, width=10)
    last_name_entry.grid(row=6, column=1, pady=10)

    date_lbl = Label(sign_up_page, text="Date")
    date_lbl.grid(row=7, column=1, pady=10)

    date_scale_month = Scale(sign_up_page, from_=1, to=12, orient=HORIZONTAL)
    date_scale_month.grid(row=8, column=1, pady=10)

    date_scale_month = Scale(sign_up_page, from_=1, to=31, orient=HORIZONTAL)
    date_scale_month.grid(row=9, column=1, pady=10)

    date_scale_month = Scale(sign_up_page, from_=1920, to=2020, orient=HORIZONTAL)
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
    next_btn.grid(row=5, column=2, ipadx=5, ipady=10)


def start_page_create():
    start_btn = Button(start_page, text='Start', command=lambda: choosing_player_page.tkraise())
    start_btn.grid(row=1, column=1, ipadx=5, ipady=10)


def choosing_player_page_create():
    choose_player_lbl = Label(choosing_player_page, text='Pick a player that you want to predict its future performance.')
    choose_player_lbl.grid(row=0, column=1)

    r = StringVar()
    r.get()

    def when_clicked(player):
        selected_player = Label(choosing_player_page, text=f"Selected player: {player}")
        selected_player.grid(row=9, column=1)

    Player_1 = Radiobutton(choosing_player_page, text="Munetaka Murakami No.55 Infielder", variable=r, value="Munetaka Murakami", command=lambda: when_clicked(r.get()))
    Player_1.grid(row=1, column=1)

    Player_2 = Radiobutton(choosing_player_page, text="Tetsuto Yamada No.1 Infielder", variable=r, value="Tetsuto Yamada", command=lambda: when_clicked(r.get()))
    Player_2.grid(row=2, column=1)

    Player_3 = Radiobutton(choosing_player_page, text="Domingo Santana No.25 Outfielder", variable=r, value="Domingo Santana", command=lambda: when_clicked(r.get()))
    Player_3.grid(row=3, column=1)

    Player_4 = Radiobutton(choosing_player_page, text="Jose Osuna No.13 Infielder", variable=r, value="Jose Osuna", command=lambda: when_clicked(r.get()))
    Player_4.grid(row=4, column=1)

    Player_5 = Radiobutton(choosing_player_page, text="Nori Aoki No.23 Outfielder", variable=r, value="Nori Aoki", command=lambda: when_clicked(r.get()))
    Player_5.grid(row=5, column=1)

    Player_6 = Radiobutton(choosing_player_page, text="Yasutaka Shiomi No.9 Outfielder", variable=r, value="Yasutaka Shiomi", command=lambda: when_clicked(r.get()))
    Player_6.grid(row=6, column=1)

    Player_7 = Radiobutton(choosing_player_page, text="Yuhei Nakamura No.27 Catcher", variable=r, value="Yuhei Nakamura", command=lambda: when_clicked(r.get()))
    Player_7.grid(row=7, column=1)

    Player_8 = Radiobutton(choosing_player_page, text="Hideki Nagaoka No.7 Infielder", variable=r, value="Hideki Nagaoka", command=lambda: when_clicked(r.get()))
    Player_8.grid(row=8, column=1)

    back_btn = Button(choosing_player_page, text='Back', command=lambda: start_page.tkraise())
    back_btn.grid(row=10, column=0, ipadx=5, ipady=10)

    next_btn = Button(choosing_player_page, text='Next', command=lambda: start_page.tkraise())
    next_btn.grid(row=10, column=2, ipadx=10, ipady=10)


def choosing_year_page_create():
    Year = Label(choosing_year_page, text='How many numbers of years of data do you want the system to use to')
    Year.grid(row=1, column=1)

    date_scale_month = Scale(sign_up_page, from_=3, to=5, orient=HORIZONTAL)
    date_scale_month.grid(row=2, column=1, pady=10)


home_page_create()
sign_up_page_create()
sign_up_page_2_create()
login_create()
start_page_create()
choosing_player_page_create()
choosing_year_page_create()

root.mainloop()