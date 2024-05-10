from tkinter import *
import sqlite3

root = Tk()
root.title("An application for a prediction of a baseball player's future contribution to the team")

# Create a database 1
conn_1 = sqlite3.connect('logins.db')

# Create a cursor for database 1
c1 = conn_1.cursor

# Create a database 2
conn_2 = sqlite3.connect('past_data.db')

# Create a cursor for database 2
c2 = conn_2.cursor

# Create a table
c1.execute("""CREATE TABLE IF NOT EXISTS logins (
        ID_number integer, 
        first_name text,
        last_name text,
        email_address text,
        data_of_birth date,
        telephone_number integer,
        username text,
        password text
        )""")

conn_1.commit()

c2.execute("""CREATE TABLE if NOT EXISTS past_data (
        ID_number integer,
        player_first_name text,
        player_last_name text,
        batting_average_2019 float,
        homeruns_2019 integer,
        RBIs_2019 integer,
        batting_average_2020 float,
        homeruns_2020 integer,
        RBIs_2020 integer,
        batting_average_2021 float,
        homeruns_2021 integer,
        RBIs_2021 integer,
        batting_average_2022 float,
        homeruns_2022 integer,
        RBIs_2022 integer,
        batting_average_2023 float,
        homeruns_2023 integer,
        RBIs_2023 integer,
        )""")

def ID_set_up():
    pass

def signup():
    pass

def login(username,password):
    pass

def menu():
    pass

# Create buttons
start_btn = Button(root, text = 'Start')
start_btn.grid(row = 0, column = 1)

menu_btn = Button(root, text = 'menu')
menu_btn.grid(row = 2, column = 0)

root.mainloop()

conn_1.commit()

conn_2.commit()

conn_1.close()

conn_2.close()