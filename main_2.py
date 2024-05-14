from tkinter import *
import sqlite3
root = Tk()

root.title("An application for a prediction of a baseball player's future contribution to the team")

# Create a database 1
conn_1 = sqlite3.connect('logins.db')

conn_2 = sqlite3.connect('past_data.db')

# Create a cursor
c1 = conn_1.cursor()

c2 = conn_2.cursor()

c1.execute('''CREATE TABLE if NOT EXISTS login (
        ID text,
        email_address text,
        first_name text,
        last_name text,
        date_of_birth date,
        telephone integer,
        username text,
        password text
        )''')

conn_1.commit()

c2.execute("""CREATE TABLE if NOT EXISTS past_data (
        ID_number integer,
        player_first_name text,
        player_last_name text,
        batting_average_2019 float,
        home_runs_2019 integer,
        RBIs_2019 integer,
        batting_average_2020 float,
        home_runs_2020 integer,
        RBIs_2020 integer,
        batting_average_2021 float,
        home_runs_2021 integer,
        RBIs_2021 integer,
        batting_average_2022 float,
        home_runs_2022 integer,
        RBIs_2022 integer,
        batting_average_2023 float,
        home_runs_2023 integer,
        RBIs_2023 integer,
        )""")
conn_2.commit()

def id_set_up():
    c1.execute("SELECT ID * FROM login")
    records = c1.fetchall()
    number = 1
    for _ in records:
        number += 1
    return number

def signup():
    pass

def login(username,email_address,password):
    records_username = c1.fetchall()[5]
    records_email_address = c1.fetchall()[0]
    records_password = c1.fetchall()[6]
    if (records_username == username or records_email_address == email_address) and records_password == password:
        pass
    else:
        error()


def error():
    print("(Username, email address) or password is incorrect")

def menu():
    pass

# Create buttons
start_btn = Button(root, text = 'Start')
start_btn.grid(row = 0, column = 1)

menu_btn = Button(root, text = 'menu')
menu_btn.grid(row = 2, column = 0)

back_btn = Button(root, text = 'Back')
back_btn.pack(side = root.LEFT, padx = 10)

back_btn = Button(root, text = 'Back')
back_btn.pack(side = root.LEFT, padx = 10)

root.mainloop()

conn_1.commit()

conn_2.commit()

conn_1.close()

conn_2.close()