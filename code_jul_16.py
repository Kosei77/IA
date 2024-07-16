from tkinter import *
from tkinter import ttk
import sqlite3
root = Tk()
root.geometry("1000x1000")

root.title("A player contribution simulator")

# Database for 2024
conn_1 = sqlite3.connect('2024_stats.db')

c_1 = conn_1.cursor()

c_1.execute("""CREATE TABLE if NOT EXISTS stats_a (
        Player_name text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        injury_period integer
        )""")

conn_1.commit()

conn_1.close()

# Database for 2023
conn_2 = sqlite3.connect('2023_stats.db')

c_2 = conn_2.cursor()

c_2.execute("""CREATE TABLE if NOT EXISTS stats_b (
        Player_name text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer,
        injury_period integer
        )""")

stat_2023 = [["Munetaka Murakami", 496, 127, 0.256, 31, 84, 0], ["Tetsuto Yamada", 376, 87, 0.231, 14, 40, 30], ["Domingo Santana", 467, 140, 0.300, 18, 66, 0], ["Jose Osuna", 501, 127, 0.253, 23, 71, 10],
             ["Nori Aoki", 217, 55, 0.253, 3, 19, 0], ["Yasutaka Shiomi", 186, 56, 0.301, 8, 31, 91], ["Yuhei Nakamura", 310, 70, 0.226, 4, 33, 7],["Hideki Nagaoka", 445, 101, 0.227, 3, 35, 0]]

c_2.execute("SELECT * from stats_b")
if c_2.fetchall() == []:
    for player_2 in stat_2023:
            c_2.execute("INSERT INTO stats_b VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI,:injury_period)",
            {
                        'player_name': player_2[0],
                        'at_bat': player_2[1],
                        'number_of_hits': player_2[2],
                        'batting_average': player_2[3],
                        'homeruns': player_2[4],
                        'RBI': player_2[5],
                        'injury_period': player_2[6],
                })

c_2.execute("SELECT * from stats_b")
print(c_2.fetchall())

conn_2.commit()

conn_2.close()

# Database for 2022
conn_3 = sqlite3.connect('2022_stats.db')

c_3 = conn_3.cursor()

c_3.execute("""CREATE TABLE if NOT EXISTS stats_c (
        Player_name text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

stat_2022 = [["Munetaka Murakami", 487, 155, 0.318, 56, 134],["Tetsuto Yamada", 469, 114, 0.243, 23, 65],["Domingo Santana", 189, 52, 0.275, 15, 35],["Jose Osuna", 496, 135, 0.272, 20, 74],
             ["Nori Aoki", 222, 55, 0.248, 5, 22], ["Yasutaka Shiomi", 508, 140, 0.276, 16, 54], ["Yuhei Nakamura", 266, 70, 0.263, 5, 28], ["Hideki Nagaoka", 511, 123, 0.241, 9, 48]]

c_3.execute("SELECT * from stats_c")
if c_3.fetchall() == []:
    for player_3 in stat_2022:
            c_3.execute("INSERT INTO stats_c VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': player_3[0],
                        'at_bat': player_3[1],
                        'number_of_hits': player_3[2],
                        'batting_average': player_3[3],
                        'homeruns': player_3[4],
                        'RBI': player_3[5],
                })

c_3.execute("SELECT * from stats_c")
print(c_3.fetchall())

conn_3.commit()

conn_3.close()

# Database for 2021
conn_4 = sqlite3.connect('2021_stats.db')

c_4 = conn_4.cursor()

c_4.execute("""CREATE TABLE if NOT EXISTS stats_d (
        Player_name text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

stat_2021 = [["Munetaka Murakami", 500, 139, 0.278, 39, 112], ["Tetsuto Yamada", 493, 134, 0.272, 34, 101], ["Domingo Santana", 372, 108, 0.290, 19, 62],  ["Jose Osuna", 469, 121, 0.258, 13, 60],
             ["Nori Aoki", 446, 115, 0.258, 9, 56],  ["Yasutaka Shiomi", 474, 132, 0.278, 14, 59], ["Yuhei Nakamura", 377, 105, 0.279, 2, 36]]

c_4.execute("SELECT * from stats_d")
if c_4.fetchall() == []:
    for player_4 in stat_2021:
            c_4.execute("INSERT INTO stats_d VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': player_4[0],
                        'at_bat': player_4[1],
                        'number_of_hits': player_4[2],
                        'batting_average': player_4[3],
                        'homeruns': player_4[4],
                        'RBI': player_4[5],
                })

c_4.execute("SELECT * from stats_d")
print(c_4.fetchall())

conn_4.commit()

conn_4.close()


# Database for 2020
conn_5 = sqlite3.connect('2020_stats.db')

c_5 = conn_5.cursor()

c_5.execute("""CREATE TABLE if NOT EXISTS stats_e (
        Player_name text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

stat_2020 = [["Munetaka Murakami", 424, 130, 0.307, 28, 86], ["Tetsuto Yamada", 344, 85, 0.254, 12, 52], ["Nori Aoki", 357, 113, 0.317, 18, 51],
             ["Yasutaka Shiomi", 154, 43, 0.279, 8, 21], ["Yuhei Nakamura", 80, 14, 0.175, 0, 3]]

c_5.execute("SELECT * from stats_e")
if c_5.fetchall() == []:
    for player_5 in stat_2020:
            c_5.execute("INSERT INTO stats_e VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': player_5[0],
                        'at_bat': player_5[1],
                        'number_of_hits': player_5[2],
                        'batting_average': player_5[3],
                        'homeruns': player_5[4],
                        'RBI': player_5[5]
                })

c_5.execute("SELECT * from stats_e")
print(c_5.fetchall())

conn_5.commit()

conn_5.close()

# Database for Murakami by team
conn_6 = sqlite3.connect('Murakami_stats_by_team.db')

c_6 = conn_6.cursor()

c_6.execute("""CREATE TABLE if NOT EXISTS stats_one (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")

stat_Murakami = [["DeNA 2024", 52, 20, 0.385, 4, 12],["Chunichi 2024", 43, 12, 0.279, 4, 9],["Hanshin 2024", 43, 10, 0.233, 2, 5],["Hirosima 2024", 32, 5, 0.156, 1, 2],["Yomiuri 2024", 46, 8, 0.174, 2, 6],
                 ["DeNA 2023", 88, 26, 0.295, 8, 21],["Chunichi 2023", 76, 22, 0.289, 6, 17],["Hanshin 2023", 90, 22, 0.244, 4, 11],["Hirosima 2023", 87, 24, 0.276, 8, 18],["Yomiuri 2023", 94, 16, 0.170, 3, 10],
                 ["DeNA 2022", 84, 28, 0.333, 9, 24],["Chunichi 2022", 88, 32, 0.364, 13, 26],["Hanshin 2022", 77, 20, 0.260, 7, 17],["Hirosima 2022", 94, 32, 0.340, 13, 26],["Yomiuri 2022", 87, 23, 0.264, 8, 28],
                 ["DeNA 2021", 85, 26, 0.306, 6, 17],["Chunichi 2021", 91, 25, 0.275, 8, 20],["Hanshin 2021", 88, 25, 0.284, 6, 17],["Hirosima 2021", 92, 20, 0.217, 4, 19],["Yomiuri 2021", 89, 31, 0.348, 8, 25],
                 ["DeNA 2020", 84, 27, 0.321, 6, 15],["Chunichi 2020", 85, 21, 0.247, 4, 15],["Hanshin 2020", 87, 32, 0.368, 5, 19],["Hirosima 2020", 81, 24, 0.296, 8, 25],["Yomiuri 2020", 87, 26, 0.299, 5, 12]]

c_6.execute("SELECT * from stats_one")
if c_6.fetchall() == []:
    for team_year_1 in stat_Murakami:
            c_6.execute("INSERT INTO stats_one VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_1[0],
                        'at_bat': team_year_1[1],
                        'number_of_hits': team_year_1[2],
                        'batting_average': team_year_1[3],
                        'homeruns': team_year_1[4],
                        'RBI': team_year_1[5]
                })

c_6.execute("SELECT * from stats_one")
print(c_6.fetchall())

conn_6.commit()

conn_6.close()

# Database for Yamada by team
conn_7 = sqlite3.connect('Yamada_stats_by_team.db')

c_7 = conn_7.cursor()

c_7.execute("""CREATE TABLE if NOT EXISTS stats_two (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Yamada = [["DeNA 2024", 22, 3, 0.136, 0, 1],["Chunichi 2024", 16, 4, 0.250, 0, 0],["Hanshin 2024", 20, 4, 0.250, 0, 3],["Hirosima 2024", 13, 1, 0.077, 0, 1],["Yomiuri 2024", 33, 7, 0.212, 0, 0],
                 ["DeNA 2023", 56, 18, 0.321, 2, 5],["Chunichi 2023", 60, 9, 0.150, 1, 6],["Hanshin 2023", 73, 15, 0.205, 4, 9],["Hirosima 2023", 54, 16, 0.296, 2, 5],["Yomiuri 2023", 64, 17, 0.266, 3, 7],
                 ["DeNA 2022", 86, 25, 0.291, 4, 9],["Chunichi 2022", 87, 17, 0.195, 2, 13],["Hanshin 2022", 71, 17, 0.239, 3, 7],["Hirosima 2022", 76, 23, 0.303, 5, 13],["Yomiuri 2022", 90, 23, 0.256, 4, 16],
                 ["DeNA 2021", 84, 24, 0.286, 6, 21],["Chunichi 2021"],["Hanshin 2021"],["Hirosima 2021"],["Yomiuri 2021"],
                 ["DeNA 2020"],["Chunichi 2020"],["Hanshin 2020"],["Hirosima 2020"],["Yomiuri 2020"]]

# Database for Santana by team
conn_8 = sqlite3.connect('Santana_stats_by_team.db')

c_8 = conn_8.cursor()

c_8.execute("""CREATE TABLE if NOT EXISTS stats_three (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Santana = [["DeNA 2024"],["Chunichi 2024"],["Hanshin 2024"],["Hirosima 2024"],["Yomiuri 2024"],
                 ["DeNA 2023"],["Chunichi 2023"],["Hanshin 2023"],["Hirosima 2023"],["Yomiuri 2023"],
                 ["DeNA 2022"],["Chunichi 2022"],["Hanshin 2022"],["Hirosima 2022"],["Yomiuri 2022"],
                 ["DeNA 2021"],["Chunichi 2021"],["Hanshin 2021"],["Hirosima 2021"],["Yomiuri 2021"],
                 ["DeNA 2020"],["Chunichi 2020"],["Hanshin 2020"],["Hirosima 2020"],["Yomiuri 2020"]]

# Database for Osuna by team
conn_9 = sqlite3.connect('Osuna_stats_by_team.db')

c_9 = conn_9.cursor()

c_9.execute("""CREATE TABLE if NOT EXISTS stats_four (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Osuna = [["DeNA 2024"],["Chunichi 2024"],["Hanshin 2024"],["Hirosima 2024"],["Yomiuri 2024"],
                 ["DeNA 2023"],["Chunichi 2023"],["Hanshin 2023"],["Hirosima 2023"],["Yomiuri 2023"],
                 ["DeNA 2022"],["Chunichi 2022"],["Hanshin 2022"],["Hirosima 2022"],["Yomiuri 2022"],
                 ["DeNA 2021"],["Chunichi 2021"],["Hanshin 2021"],["Hirosima 2021"],["Yomiuri 2021"],
                 ["DeNA 2020"],["Chunichi 2020"],["Hanshin 2020"],["Hirosima 2020"],["Yomiuri 2020"]]

# Database for Aoki by team
conn_10 = sqlite3.connect('Aoki_stats_by_team.db')

c_10 = conn_10.cursor()

c_10.execute("""CREATE TABLE if NOT EXISTS stats_five (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Aoki = [["DeNA 2024"],["Chunichi 2024"],["Hanshin 2024"],["Hirosima 2024"],["Yomiuri 2024"],
                 ["DeNA 2023"],["Chunichi 2023"],["Hanshin 2023"],["Hirosima 2023"],["Yomiuri 2023"],
                 ["DeNA 2022"],["Chunichi 2022"],["Hanshin 2022"],["Hirosima 2022"],["Yomiuri 2022"],
                 ["DeNA 2021"],["Chunichi 2021"],["Hanshin 2021"],["Hirosima 2021"],["Yomiuri 2021"],
                 ["DeNA 2020"],["Chunichi 2020"],["Hanshin 2020"],["Hirosima 2020"],["Yomiuri 2020"]]

# Database for Shiomi by team
conn_11 = sqlite3.connect('Shiomi_stats_by_team.db')

c_11 = conn_11.cursor()

c_11.execute("""CREATE TABLE if NOT EXISTS stats_six (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Shiomi = [["DeNA 2024"],["Chunichi 2024"],["Hanshin 2024"],["Hirosima 2024"],["Yomiuri 2024"],
                 ["DeNA 2023"],["Chunichi 2023"],["Hanshin 2023"],["Hirosima 2023"],["Yomiuri 2023"],
                 ["DeNA 2022"],["Chunichi 2022"],["Hanshin 2022"],["Hirosima 2022"],["Yomiuri 2022"],
                 ["DeNA 2021"],["Chunichi 2021"],["Hanshin 2021"],["Hirosima 2021"],["Yomiuri 2021"],
                 ["DeNA 2020"],["Chunichi 2020"],["Hanshin 2020"],["Hirosima 2020"],["Yomiuri 2020"]]

# Database for Nakamura by team
conn_12 = sqlite3.connect('Nakamura_stats_by_team.db')

c_12 = conn_12.cursor()

c_12.execute("""CREATE TABLE if NOT EXISTS stats_seven (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Nakamura = [["DeNA 2024"],["Chunichi 2024"],["Hanshin 2024"],["Hirosima 2024"],["Yomiuri 2024"],
                 ["DeNA 2023"],["Chunichi 2023"],["Hanshin 2023"],["Hirosima 2023"],["Yomiuri 2023"],
                 ["DeNA 2022"],["Chunichi 2022"],["Hanshin 2022"],["Hirosima 2022"],["Yomiuri 2022"],
                 ["DeNA 2021"],["Chunichi 2021"],["Hanshin 2021"],["Hirosima 2021"],["Yomiuri 2021"],
                 ["DeNA 2020"],["Chunichi 2020"],["Hanshin 2020"],["Hirosima 2020"],["Yomiuri 2020"]]

# Database for Nagaoka by team
conn_13 = sqlite3.connect('Nagaoka_stats_by_team.db')

c_13 = conn_13.cursor()

c_13.execute("""CREATE TABLE if NOT EXISTS stats_eight (
        Team_against_year text,
        At_bat integer,
        Number_of_hits integer,
        Batting_average real,
        Number_of_homeruns integer,
        RBI integer
        )""")
stat_Nagaoka = [["DeNA 2024", 52, 13, 0.250, 0, 4],["Chunichi 2024", 43, 6, 0.140, 0, 0],["Hanshin 2024", 47, 16, 0.340, 1, 7],["Hirosima 2024", 35, 10, 0.286, 0, 4],["Yomiuri 2024", 49, 19, 0.388, 1, 6],
                 ["DeNA 2023", 78, 15, 0.192, 1, 5],["Chunichi 2023", 82, 22, 0.268, 1, 9],["Hanshin 2023", 77, 16, 0.208, 0, 2],["Hirosima 2023", 76, 14, 0.184, 0, 9],["Yomiuri 2023", 84, 20, 0.238, 1, 6],
                 ["DeNA 2022", 81, 24, 0.296, 2, 4],["Chunichi 2022", 85, 17, 0.200, 0, 3],["Hanshin 2022", 91, 23, 0.253, 0, 6],["Hirosima 2022", 98, 23, 0.235, 3, 10],["Yomiuri 2022", 94, 21, 0.223, 4, 15]]

c_13.execute("SELECT * from stats_eight")
if c_13.fetchall() == []:
    for team_year_8 in stat_Nagaoka:
            c_13.execute("INSERT INTO stats_eight VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_8[0],
                        'at_bat': team_year_8[1],
                        'number_of_hits': team_year_8[2],
                        'batting_average': team_year_8[3],
                        'homeruns': team_year_8[4],
                        'RBI': team_year_8[5]
                })

c_13.execute("SELECT * from stats_eight")
print(c_13.fetchall())

conn_13.commit()

conn_13.close()

# Pages for the applications
start_page = Frame(root)
choosing_player_page = Frame(root)
choosing_year_page = Frame(root)
instruction_page = Frame(root)
Results_page = Frame(root)
confirmation_page = Frame(root)

frames = [start_page, choosing_player_page, choosing_year_page, Results_page, instruction_page, confirmation_page]

start_page.tkraise()

for page in frames:
    page.grid(row=0, column=0, sticky="nsew")

# Creating the start page
def start_page_create():
    start_btn = Button(start_page, text='Start', command=lambda: choosing_player_page.tkraise())
    start_btn.pack(pady=5, ipadx=10, ipady=10)

    instruction_btn = Button(start_page, text='Instruction', command=lambda: instruction_page.tkraise())
    instruction_btn.pack(pady=5, ipadx=10, ipady=10)

def choosing_player_page_create():

    def clicked():
        global player_name
        player_name = Entrys.get()
        print(player_name)
        Entrys.delete(0, END)

    choose_player_lbl = Label(choosing_player_page, text='Pick a player that you want to predict its future performance.')
    choose_player_lbl.grid(row=0, column=1)

    player_1 = Label(choosing_player_page, text="Player 1: Munetaka Murakami No.55 Infielder")
    player_1.grid(row=1, column=1)

    player_2 = Label(choosing_player_page, text="Player 2: Tetsuto Yamada No.1 Infielder")
    player_2.grid(row=2, column=1)

    player_3 = Label(choosing_player_page, text="Player 3: Domingo Santana No.25 Outfielder")
    player_3.grid(row=3, column=1)

    player_4 = Label(choosing_player_page, text="Player 4: Jose Osuna No.13 Infielder")
    player_4.grid(row=4, column=1)

    player_5 = Label(choosing_player_page, text="Player 5: Nori Aoki No.23 Outfielder")
    player_5.grid(row=5, column=1)

    player_6 = Label(choosing_player_page, text="Player 6: Yasutaka Shiomi No.9 Outfielder")
    player_6.grid(row=6, column=1)

    player_7 = Label(choosing_player_page, text="Player 7: Yuhei Nakamura No.27 Catcher")
    player_7.grid(row=7, column=1)

    player_8 = Label(choosing_player_page, text="Player 8: Hideki Nagaoka No.7 Infielder")
    player_8.grid(row=8, column=1)

    blank = Label(choosing_player_page, text="")
    blank.grid(row=9, column=1)

    Instruction = Label(choosing_player_page, text="Type in the entry below one of the player above. Type in player and the number..")
    Instruction.grid(row=10, column=1)

    Instruction = Label(choosing_player_page, text="If you want to pick Munetaka Murakami, type Player 1.")
    Instruction.grid(row=11, column=1)

    Entrys = Entry(choosing_player_page, width = 50)
    Entrys.grid(row=12, column=1)

    back_btn = Button(choosing_player_page, text='Back', command=lambda: start_page.tkraise())
    back_btn.grid(row=13, column=0, ipadx=5, ipady=10)

    submit_btn = Button(choosing_player_page, text='Submit', command= clicked)
    submit_btn.grid(row=13, column=1, ipadx=10, ipady=10)

    next_btn = Button(choosing_player_page, text='Next', command=lambda: choosing_year_page.tkraise())
    next_btn.grid(row=13, column=2, ipadx=10, ipady=10)



def choosing_year_page_create():
    year = Label(choosing_year_page, text='How many numbers of years of data do you want the system to use to')
    year.grid(row=1, column=1)

    date_scale_month = Entry(choosing_year_page, width=10)
    date_scale_month.grid(row=2, column=1, pady=10)

    back_btn = Button(choosing_year_page, text='Back', command=lambda: choosing_player_page.tkraise())
    back_btn.grid(row=3, column=0, ipadx=5, ipady=10)

    next_btn = Button(choosing_year_page, text='Next', command=lambda: Results_page.tkraise())
    next_btn.grid(row=3, column=2, ipadx=10, ipady=10)

def results_page_create():
    pass
def instruction_page_create():
    step = Label(instruction_page, text="Step by step instruction for the system")
    step.pack()
    step_three = Label(instruction_page, text="1. Click the start button on the start page.")
    step_three.pack()
    step_four = Label(instruction_page, text="2. Choose the player that you want the prediction of.")
    step_four.pack()
    step_five = Label(instruction_page, text="3. To find more information about the player and their stats, click on the button next to the name.")
    step_five.pack()
    step_six = Label(instruction_page, text="4. Choose the number of years of data the system want to use.")
    step_six.pack()
    step_seven = Label(instruction_page, text="5. The player's performance is displayed and its future too.")
    step_seven.pack()
    back_btn = Button(instruction_page, text='Back', command=lambda: start_page.tkraise())
    back_btn.pack()

start_page_create()
choosing_player_page_create()
choosing_year_page_create()
instruction_page_create()
root.mainloop()
