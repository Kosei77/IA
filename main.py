from tkinter import *
from tkinter import messagebox
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
             ["Nori Aoki", 217, 55, 0.253, 3, 19, 0], ["Yasutaka Shiomi", 186, 56, 0.301, 8, 31, 91], ["Yuhei Nakamura", 310, 70, 0.226, 4, 33, 7], ["Hideki Nagaoka", 445, 101, 0.227, 3, 35, 0]]

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
                 ["DeNA 2021", 84, 24, 0.286, 6, 21],["Chunichi 2021", 94, 28, 0.298, 7, 19],["Hanshin 2021", 86, 21, 0.244, 7, 20],["Hirosima 2021", 82, 20, 0.244, 1, 7],["Yomiuri 2021", 78, 21, 0.269, 6, 16],
                 ["DeNA 2020", 73, 18, 0.247, 1, 15],["Chunichi 2020", 64, 18, 0.281, 4, 15],["Hanshin 2020", 56, 10, 0.179, 0, 2],["Hirosima 2020", 69, 20, 0.290, 3, 6],["Yomiuri 2020", 72, 19, 0.264, 4, 14]]

c_7.execute("SELECT * from stats_two")
if c_7.fetchall() == []:
    for team_year_2 in stat_Yamada:
            c_7.execute("INSERT INTO stats_two VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_2[0],
                        'at_bat': team_year_2[1],
                        'number_of_hits': team_year_2[2],
                        'batting_average': team_year_2[3],
                        'homeruns': team_year_2[4],
                        'RBI': team_year_2[5]
                })

c_7.execute("SELECT * from stats_two")
print(c_7.fetchall())

conn_7.commit()

conn_7.close()

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
stat_Santana = [["DeNA 2024", 48, 19, 0.396, 4, 9], ["Chunichi 2024", 38, 9, 0.237, 0, 5],["Hanshin 2024",35,11,0.314,0,9],["Hirosima 2024",35,11,0.314,1,2],["Yomiuri 2024",41,14,0.341,2,7],
                 ["DeNA 2023",86,31,0.360,5,14],["Chunichi 2023",81,21,0.259,3,6],["Hanshin 2023",81,23,0.284,3,6],["Hirosima 2023",71,20,0.282,3,18],["Yomiuri 2023",81,27,0.333,2,10],
                 ["DeNA 2022",33,6,0.182,1,2],["Chunichi 2022",46,13,0.283,3,10],["Hanshin 2022",42,11,0.262,3,8],["Hirosima 2022",33,10,0.303,2,3],["Yomiuri 2022",35,12,0.343,6,12],
                 ["DeNA 2021", 54,16,0.296,3,10],["Chunichi 2021",68,19,0.279,3,8],["Hanshin 2021",64,21,0.328,1,12],["Hirosima 2021",56,12,0.214,3,8],["Yomiuri 2021",71,22,0.310,8,19]]

c_8.execute("SELECT * from stats_three")
if c_8.fetchall() == []:
    for team_year_3 in stat_Santana:
            c_8.execute("INSERT INTO stats_three VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_3[0],
                        'at_bat': team_year_3[1],
                        'number_of_hits': team_year_3[2],
                        'batting_average': team_year_3[3],
                        'homeruns': team_year_3[4],
                        'RBI': team_year_3[5]
                })

c_8.execute("SELECT * from stats_three")
print(c_8.fetchall())

conn_8.commit()

conn_8.close()

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
stat_Osuna = [["DeNA 2024",55,12,0.218,1,6],["Chunichi 2024",52,15,0.288,2,10],["Hanshin 2024",50,9,0.180,2,6],["Hirosima 2024",35,9,0.257,1,4],["Yomiuri 2024",52,15,0.288,1,6],
                 ["DeNA 2023",100,30,0.300,3,12],["Chunichi 2023",85,18,0.212,2,9],["Hanshin 2023",79,13,0.165,1,5],["Hirosima 2023",83,21,0.253,5,13],["Yomiuri 2023",88,29,0.330,8,20],
                 ["DeNA 2022",82,27,0.329,6,16],["Chunichi 2022",90,21,0.233,2,11],["Hanshin 2022",82,16,0.195,1,8],["Hirosima 2022",80,23,0.288,4,12],["Yomiuri 2022",100,30,0.300,5,20],
                 ["DeNA 2021",70,14,0.200,4,10],["Chunichi 2021",88,26,0.295,2,10],["Hanshin 2021",81,19,0.235,0,8],["Hirosima 2021",71,21,0.296,2,8],["Yomiuri 2021",89,20,0.225,4,17]]

c_9.execute("SELECT * from stats_four")
if c_9.fetchall() == []:
    for team_year_4 in stat_Osuna:
            c_9.execute("INSERT INTO stats_four VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_4[0],
                        'at_bat': team_year_4[1],
                        'number_of_hits': team_year_4[2],
                        'batting_average': team_year_4[3],
                        'homeruns': team_year_4[4],
                        'RBI': team_year_4[5]
                })

c_9.execute("SELECT * from stats_four")
print(c_9.fetchall())

conn_9.commit()

conn_9.close()

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
stat_Aoki = [["DeNA 2024",23,3,0.130,0,3],["Chunichi 2024",11,2,0.182,0,1],["Hanshin 2024",8,4,0.500,0,1],["Hirosima 2024",10,2,0.200,0,0],["Yomiuri 2024",13,0,0.000,0,1],
                 ["DeNA 2023",24,5,0.208,1,5],["Chunichi 2023",29,5,0.172,0,1],["Hanshin 2023",31,6,0.194,0,2],["Hirosima 2023",34,7,0.206,0,2],["Yomiuri 2023",42,17,0.405,0,2],
                 ["DeNA 2022",36,9,0.250,1,4],["Chunichi 2022",36,8,0.222,0,1],["Hanshin 2022",58,14,0.241,2,5],["Hirosima 2022",36,8,0.222,1,4],["Yomiuri 2022",49,13,0.265,1,7],
                 ["DeNA 2021",68,12,0.176,1,9],["Chunichi 2021",78,13,0.167,0,9],["Hanshin 2021",92,23,0.250,1,7],["Hirosima 2021",73,28,0.384,2,11],["Yomiuri 2021",74,18,0.243,2,8],
                 ["DeNA 2020",81,27,0.333,4,14],["Chunichi 2020",69,16,0.232,3,4],["Hanshin 2020",77,27,0.351,2,6],["Hirosima 2020",60,21,0.350,3,12],["Yomiuri 2020",70,22,0.314,6,15]]

c_10.execute("SELECT * from stats_five")
if c_10.fetchall() == []:
    for team_year_5 in stat_Aoki:
            c_10.execute("INSERT INTO stats_five VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_5[0],
                        'at_bat': team_year_5[1],
                        'number_of_hits': team_year_5[2],
                        'batting_average': team_year_5[3],
                        'homeruns': team_year_5[4],
                        'RBI': team_year_5[5]
                })

c_10.execute("SELECT * from stats_five")
print(c_10.fetchall())

conn_10.commit()

conn_10.close()

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
stat_Shiomi = [["DeNA 2024",28,6,0.214,0,3],["Chunichi 2024",31,9,0.290,2,3],["Hanshin 2024",12,3,0.250,1,1],["Hirosima 2024",16,4,0.250,0,1],["Yomiuri 2024",14,5,0.357,0,0],
                 ["DeNA 2023",49,16,0.327,2,4],["Chunichi 2023",24,9,0.375,1,7],["Hanshin 2023",47,10,0.213,2,6],["Hirosima 2023",28,11,0.393,0,7],["Yomiuri 2023",38,10,0.263,3,7],
                 ["DeNA 2022",85,22,0.259,3,11],["Chunichi 2022",91,21,0.231,0,3],["Hanshin 2022",81,17,0.210,1,6],["Hirosima 2022",90,31,0.344,3,16],["Yomiuri 2022",86,26,0.302,4,7],
                 ["DeNA 2021",92,25,0.272,3,16],["Chunichi 2021",73,21,0.288,1,5],["Hanshin 2021",63,18,0.286,1,9],["Hirosima 2021",80,19,0.238,2,9],["Yomiuri 2021",91,26,0.286,3,13],
                 ["DeNA 2020",10,4,0.400,1,2],["Chunichi 2020",44,13,0.295,4,9],["Hanshin 2020",34,7,0.206,2,6],["Hirosima 2020",35,11,0.314,0,2],["Yomiuri 2020",31,8,0.258,1,2]]

c_11.execute("SELECT * from stats_six")
if c_11.fetchall() == []:
    for team_year_6 in stat_Shiomi:
            c_11.execute("INSERT INTO stats_six VALUES (:player_name, :at_bat, :number_of_hits,:batting_average,:homeruns,:RBI)",
            {
                        'player_name': team_year_6[0],
                        'at_bat': team_year_6[1],
                        'number_of_hits': team_year_6[2],
                        'batting_average': team_year_6[3],
                        'homeruns': team_year_6[4],
                        'RBI': team_year_6[5]
                })

c_11.execute("SELECT * from stats_six")
print(c_11.fetchall())

conn_11.commit()

conn_11.close()

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

conn_12.commit()

conn_12.close()

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

# Database for opponent win-lose performance
conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
c_14 = conn_14.cursor()

c_14.execute("""CREATE TABLE if NOT EXISTS stats_win_lose (
        Team_against_year text,
        Win_number integer,
        Lose_number integer
        )""")
stat_win_lose = [["All 2024", 34, 46],["DeNA 2024", 5, 10],["Chunichi 2024", 7, 5],["Hanshin 2024", 5, 8],["Hirosima 2024", 2, 9],["Yomiuri 2024", 6, 8],
                 ["All 2023", 57, 83],["DeNA 2023", 10, 14],["Chunichi 2023", 14, 11],["Hanshin 2023", 7, 17],["Hirosima 2023", 11, 13],["Yomiuri 2023", 8, 17],
                 ["All 2022", 80, 59],["DeNA 2022", 16, 9],["Chunichi 2022", 10, 14],["Hanshin 2022", 13, 11],["Hirosima 2022", 16, 8],["Yomiuri 2022", 11, 13],
                 ["All 2021", 73, 52],["DeNA 2021", 17, 6],["Chunichi 2021", 13, 6],["Hanshin 2021", 8, 13],["Hirosima 2021", 14, 8],["Yomiuri 2021", 14, 11],
                 ["All 2020", 41, 69],["DeNA 2020", 11, 12],["Chunichi 2020", 7, 15],["Hanshin 2020", 10, 13],["Hirosima 2020", 7, 14],["Yomiuri 2020", 6, 15]]

c_14.execute("SELECT * from stats_win_lose")
if c_14.fetchall() == []:
    for lose_win in stat_win_lose:
            c_14.execute("INSERT INTO stats_win_lose VALUES (:Team_against_year, :Win_number, :Lose_number)",
            {
                        'Team_against_year': lose_win[0],
                        'Win_number': lose_win[1],
                        'Lose_number': lose_win[2],
                })

c_14.execute("SELECT * from stats_win_lose")
print(c_14.fetchall())

conn_14.commit()

conn_14.close()

# Database for opponent pitcher and fielding performace
conn_15 = sqlite3.connect('pitcher_fieldr_by_opponent.db')
c_15 = conn_15.cursor()


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
start_btn = Button(start_page, text='Start', command=lambda: choosing_player_page.tkraise())
start_btn.grid(row=0, column=0)

instruction_btn = Button(start_page, text='Instruction', command=lambda: instruction_page.tkraise())
instruction_btn.grid(row=1, column=0)


def clicked():
    player_name = Entrys.get()
    player_name = player_name.lower()
    if player_name == 'player 1' or player_name == 'player 2' or player_name == 'player 3' or player_name == 'player 4' or player_name == 'player 5' or player_name == 'player 6' or player_name == 'player 7' or player_name == 'player 8':
        Entrys.delete(0, END)
        player_number_name = {'player 1': 'Munetaka Murakami No.55 Infielder', 'player 2': 'Tetsuto Yamada No.1 Infielder', 'player 3': 'Domingo Santana No.25 Outfielder', 'player 4': 'Jose Osuna No.13 Infielder', 'player 5': 'Nori Aoki No.23 Outfielder', 'player 6': 'Yasutaka Shiomi No.9 Outfielder', 'player 7': 'Yuhei Nakamura No.27 Catcher', 'player 8': 'Hideki Nagaoka No.7 Infielder'}
        print(player_number_name[player_name])
        confirms_2.config(text=player_number_name[player_name])
    else:
        messagebox.showwarning("Type in error", "Please type in the correct input from player 1 to player 8")

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

Instruction_2 = Label(choosing_player_page, text="If you want to pick Munetaka Murakami, type Player 1.")
Instruction_2.grid(row=11, column=1)

Entrys = Entry(choosing_player_page, width = 50)
Entrys.grid(row=12, column=1)

back_btn = Button(choosing_player_page, text='Back', command=lambda: start_page.tkraise())
back_btn.grid(row=13, column=0, ipadx=5, ipady=10)

submit_btn = Button(choosing_player_page, text='Submit', command= clicked)
submit_btn.grid(row=13, column=1, ipadx=10, ipady=10)

next_btn = Button(choosing_player_page, text='Next', command=lambda: choosing_year_page.tkraise())
next_btn.grid(row=13, column=2, ipadx=10, ipady=10)


def clicked():
    years = date_scale_month.get()
    try:
        years = int(years)
        if years >= 3 and years <= 5:
            date_scale_month.delete(0, END)
            confirms_2.config(text=f"Number of past years used is {years} years")
            print(years)
        else:
                messagebox.showwarning("Type in error", "Please type in the number of years between 3 to 5")
    except:
        messagebox.showwarning("Type in error", "Please type in the number of years between 3 to 5")

year = Label(choosing_year_page, text='How many numbers of years of data do you want the system to use to')
year.grid(row=1, column=1)

date_scale_month = Entry(choosing_year_page, width=10)
date_scale_month.grid(row=2, column=1, pady=10)

back_btn = Button(choosing_year_page, text='Back', command=lambda: choosing_player_page.tkraise())
back_btn.grid(row=3, column=0, ipadx=5, ipady=10)

next_btn = Button(choosing_year_page, text='Next', command=lambda: confirmation_page.tkraise())
next_btn.grid(row=3, column=2, ipadx=10, ipady=10)

submit_btn = Button(choosing_year_page, text='Submit', command=clicked)
submit_btn.grid(row=3, column=1, ipadx=10, ipady=10)

confirm = Label(confirmation_page, text='Please confirm the information below is correct')
confirm.grid(row=0, column=1)
confirms_1 = Label(confirmation_page)
confirms_1.grid(row=1, column=1)
confirms_2 = Label(confirmation_page)
confirms_2.grid(row=2, column=1)
back_btn = Button(confirmation_page, text='Back', command=lambda: choosing_year_page.tkraise())
back_btn.grid(row=3, column=0)
next_btn = Button(confirmation_page, text='Next', command=lambda: Results_page.tkraise())
next_btn.grid(row=3, column=2)

def calculation(player, year):
    number_to_player = {'player 1': 0, 'player 2': 1, 'player 3': 2, 'player 4': 3, 'player 5': 4, 'player 6': 5, 'player 7': 6, 'player 8': 7}
    index = number_to_player[player]
    conn_1 = sqlite3.connect('2024_stats.db')
    c_1 = conn_1.cursor()
    conn_2 = sqlite3.connect('2023_stats.db')
    c_2 = conn_2.cursor()
    conn_3 = sqlite3.connect('2022_stats.db')
    c_3 = conn_3.cursor()
    conn_4 = sqlite3.connect('2021_stats.db')
    c_4 = conn_4.cursor()
    conn_5 = sqlite3.connect('2020_stats.db')
    c_5 = conn_5.cursor()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()

    c_2.execute("SELECT * from stats_b")
    c_3.execute("SELECT * from stats_c")
    c_4.execute("SELECT * from stats_d")
    c_5.execute("SELECT * from stats_e")
    c_14.execute("SELECT * from stats_win_lose")

    if year == 3 or index == 7:
        data_win = c_14.fetchall()
        data_2023 = c_2.fetchall()
        data_2022 = c_3.fetchall()
        total_percentage = (data_win[0][1]+data_win[6][1]+data_win[12][1])/(data_win[0][1]+data_win[6][1]+data_win[12][1] + data_win[0][2]+data_win[6][2]+data_win[12][2])
        bat_2023, hit_2023, homerun_2023, RBI_2023, injury_2023 = data_2023[index][1], data_2023[index][2],data_2023[index][4], data_2023[index][5], data_2023[index][6]
        bat_2022, hit_2022, homerun_2022, RBI_2022 = data_2022[index][1], data_2022[index][2], data_2022[index][4], data_2022[index][5]

        batting = (hit_2023 + hit_2022) / (bat_2023 + bat_2022)

        prob_4_4 = (batting ** 4)
        prob_4_3 = (batting ** 3) * (1 - batting) * 4
        prob_4_2 = (batting ** 2) * ((1 - batting) ** 2) * 6
        prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

        RBI_to_hit_ratio = (RBI_2023 + RBI_2022) / (hit_2023 + hit_2022)
        Homerun_to_hit_ratio = (homerun_2023 + homerun_2022) / (hit_2023 + hit_2022)

        predicted_total_games_played = 143 - injury_2023
        total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
        total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio
        total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio

        f = RBI_to_hit_ratio

        Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played

        print(int(Total_number_of_games_contribution*total_percentage))

    elif year == 4 or index == 3 or index == 2:
        data_win = c_14.fetchall()
        data_2023 = c_2.fetchall()
        data_2022 = c_3.fetchall()
        data_2021 = c_4.fetchall()
        total_percentage = (data_win[0][1] + data_win[6][1] + data_win[12][1] + data_win[18][1]) / (data_win[0][1] + data_win[6][1] + data_win[12][1] + data_win[18][1] + data_win[0][2] + data_win[6][2] + data_win[12][2] + data_win[18][2])
        bat_2023, hit_2023, homerun_2023, RBI_2023, injury_2023 = data_2023[index][1], data_2023[index][2], data_2023[index][4], data_2023[index][5], data_2023[index][6]
        bat_2022, hit_2022, homerun_2022, RBI_2022 = data_2022[index][1], data_2022[index][2], data_2022[index][4], data_2022[index][5]
        bat_2021, hit_2021, homerun_2021, RBI_2021 = data_2021[index][1], data_2021[index][2], data_2021[index][4], data_2021[index][5]

        batting = (hit_2023 + hit_2022 + hit_2021) / (bat_2023 + bat_2022 + bat_2021)

        prob_4_4 = (batting**4)
        prob_4_3 = (batting**3)*(1-batting)*4
        prob_4_2 = (batting**2)*((1-batting)**2)*6
        prob_4_1 = (batting)*((1-batting)**3)*4

        RBI_to_hit_ratio = (RBI_2023 + RBI_2022 + RBI_2021) / (hit_2023 + hit_2022 + hit_2021)
        Homerun_to_hit_ratio = (homerun_2023 + homerun_2022 + homerun_2021) / (hit_2023 + hit_2022 + hit_2021)

        predicted_total_games_played = 143 - injury_2023
        total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
        total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio
        total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio

        f = RBI_to_hit_ratio

        Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
        print(int(Total_number_of_games_contribution*total_percentage))


    else:
        data_win = c_14.fetchall()
        data_2023 = c_2.fetchall()
        data_2022 = c_3.fetchall()
        data_2021 = c_4.fetchall()
        data_2020 = c_5.fetchall()
        total_percentage = (data_win[0][1] + data_win[6][1] + data_win[12][1] + data_win[18][1] + data_win[24][1]) / (data_win[0][1] + data_win[6][1] + data_win[12][1] + data_win[18][1] + data_win[24][1]+ data_win[0][2] + data_win[6][2] + data_win[12][2] + data_win[18][2] + data_win[24][2])
        bat_2023, hit_2023, homerun_2023, RBI_2023, injury_2023 = data_2023[index][1], data_2023[index][2], data_2023[index][4], data_2023[index][5], data_2023[index][6]
        bat_2022, hit_2022, homerun_2022, RBI_2022 = data_2022[index][1], data_2022[index][2], data_2022[index][4], data_2022[index][5]
        bat_2021, hit_2021, homerun_2021, RBI_2021 = data_2021[index][1], data_2021[index][2], data_2021[index][4], data_2021[index][5]
        if index == 0 or index == 1:
            bat_2020, hit_2020, homerun_2020, RBI_2020 = data_2020[index][1], data_2020[index][2], data_2020[index][4], data_2020[index][5]
        else:
            bat_2020, hit_2020, homerun_2020, RBI_2020 = data_2020[index-2][1], data_2020[index-2][2], data_2020[index-2][4], data_2020[index-2][5]

        batting = (hit_2023 + hit_2022 + hit_2021 + hit_2020) / (bat_2023 + bat_2022 + bat_2021 + bat_2020)

        prob_4_4 = (batting ** 4)
        prob_4_3 = (batting ** 3) * (1 - batting) * 4
        prob_4_2 = (batting ** 2) * ((1 - batting) ** 2) * 6
        prob_4_1 = (batting) * ((1 - batting) ** 3) * 4

        RBI_to_hit_ratio = (RBI_2023 + RBI_2022 + RBI_2021 + RBI_2020) / (hit_2023 + hit_2022 + hit_2021 + hit_2020)
        Homerun_to_hit_ratio = (homerun_2023 + homerun_2022 + homerun_2021 + homerun_2020) / (hit_2023 + hit_2022 + hit_2021 + hit_2020)

        predicted_total_games_played = 143-injury_2023
        total_predicted_hit = (predicted_total_games_played*prob_4_1)+(predicted_total_games_played*prob_4_2*2)+(predicted_total_games_played*prob_4_3*3)+(predicted_total_games_played*prob_4_4*4)
        total_predicted_RBI = total_predicted_hit*RBI_to_hit_ratio
        total_predicted_homerun = total_predicted_hit*Homerun_to_hit_ratio

        f = RBI_to_hit_ratio

        Total_number_of_games_contribution = ((prob_4_1*f) + (prob_4_2*(1-(1-f)**2))+ (prob_4_3*(1-(1-f)**3)) + (prob_4_4*(1-(1-f)**4))) * predicted_total_games_played

        print(int(Total_number_of_games_contribution * total_percentage))

    conn_1.commit()
    conn_1.close()
    conn_2.commit()
    conn_2.close()
    conn_3.commit()
    conn_3.close()
    conn_4.commit()
    conn_4.close()
    conn_5.commit()
    conn_5.close()
    conn_14.commit()
    conn_14.close()

def Murakami(year):
    conn_6 = sqlite3.connect('Murakami_stats_by_team.db')
    c_6 = conn_6.cursor()
    c_6.execute("SELECT * from stats_one")
    data = c_6.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Murakami_calculations(batting_DB, batting_D, batting_T, batting_C, batting_G, RBI_to_hit_ratio_DB,RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C, RBI_to_hit_ratio_G,Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G, win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G):
        win = [win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,RBI_to_hit_ratio_G]
        Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
        Total_number_of_games_contribution_by_team = []

        for i in range(5):
            prob_4_4 = (batting[i] ** 4)
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + ( prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
            Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))
        return (Total_number_of_games_contribution_by_team)

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = data[15][1], data[15][2], data[15][4], data[15][5]
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = data[20][1], data[20][2], data[20][4], data[20][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[11][4], data[11][5]
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = data[16][1], data[16][2], data[16][4], data[16][5]
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = data[21][1], data[21][2], data[21][4], data[21][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = data[17][1], data[17][2], data[17][4], data[17][5]
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = data[22][1], data[22][2], data[22][4], data[22][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = data[18][1], data[18][2], data[18][4], data[18][5]
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = data[23][1], data[23][2], data[23][4], data[23][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = data[19][1], data[19][2], data[19][4], data[19][5]
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = data[24][1], data[24][2], data[24][4], data[24][5]

    batting_DB_5 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB)
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB)
    RBI_to_hit_ratio_DB_5 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB_5 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB + homerun_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D)
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D)
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    RBI_to_hit_ratio_D_5 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D_5 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D + homerun_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T)
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T)
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    RBI_to_hit_ratio_T_5 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T_5 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T + homerun_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C)
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C)
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    RBI_to_hit_ratio_C_5 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C_5 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C + homerun_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G)
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G)
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)
    RBI_to_hit_ratio_G_5 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G_5 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G + homerun_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_4_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[1][2] + data_win[7][2] + data_win[13][2] + data_win[19][2])
    win_percentage_5_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1] + data_win[1][2] + data_win[7][2] + data_win[13][2] + data_win[19][2] + data_win[25][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_4_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[2][2] + data_win[8][2] + data_win[14][2] + data_win[20][2])
    win_percentage_5_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1] + data_win[2][2] + data_win[8][2] + data_win[14][2] + data_win[20][2] + data_win[26][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_4_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[3][2] + data_win[9][2] + data_win[15][2] + data_win[21][2])
    win_percentage_5_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1] + data_win[3][2] + data_win[9][2] + data_win[15][2] + data_win[21][2] + data_win[27][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_4_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[4][2] + data_win[10][2] + data_win[16][2] + data_win[22][2])
    win_percentage_5_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1] + data_win[4][2] + data_win[10][2] + data_win[16][2] + data_win[22][2] + data_win[28][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])
    win_percentage_4_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[5][2] + data_win[11][2] + data_win[17][2] + data_win[23][2])
    win_percentage_5_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1] + data_win[5][2] + data_win[11][2] + data_win[17][2] + data_win[23][2] + data_win[29][2])

    if year == 5:
        x = Murakami_calculations(batting_DB_5, batting_D_5, batting_T_5, batting_C_5, batting_G_5, RBI_to_hit_ratio_DB_5,RBI_to_hit_ratio_D_5, RBI_to_hit_ratio_T_5, RBI_to_hit_ratio_C_5, RBI_to_hit_ratio_G_5,Homerun_to_hit_ratio_DB_5, Homerun_to_hit_ratio_D_5, Homerun_to_hit_ratio_T_5,Homerun_to_hit_ratio_C_5, Homerun_to_hit_ratio_G_5, win_percentage_5_DB, win_percentage_5_D, win_percentage_5_T, win_percentage_5_C, win_percentage_5_G)
        print(x)
    elif year == 4:
        x = Murakami_calculations(batting_DB_4, batting_D_4, batting_T_4, batting_C_4, batting_G_4, RBI_to_hit_ratio_DB_4,RBI_to_hit_ratio_D_4, RBI_to_hit_ratio_T_4, RBI_to_hit_ratio_C_4, RBI_to_hit_ratio_G_4,Homerun_to_hit_ratio_DB_4, Homerun_to_hit_ratio_D_4, Homerun_to_hit_ratio_T_4,Homerun_to_hit_ratio_C_4, Homerun_to_hit_ratio_G_4, win_percentage_4_DB, win_percentage_4_D, win_percentage_4_T, win_percentage_4_C, win_percentage_4_G)
        print(x)
    elif year == 3:
        x = Murakami_calculations(batting_DB_3, batting_D_3, batting_T_3, batting_C_3, batting_G_3, RBI_to_hit_ratio_DB_3,RBI_to_hit_ratio_D_3, RBI_to_hit_ratio_T_3, RBI_to_hit_ratio_C_3, RBI_to_hit_ratio_G_3,Homerun_to_hit_ratio_DB_3, Homerun_to_hit_ratio_D_3, Homerun_to_hit_ratio_T_3,Homerun_to_hit_ratio_C_3, Homerun_to_hit_ratio_G_3, win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T, win_percentage_3_C, win_percentage_3_G)
        print(x)

    conn_6.commit()
    conn_6.close()
    conn_14.commit()
    conn_14.close()

def Yamada(year):
    conn_7 = sqlite3.connect('Yamada_stats_by_team.db')
    c_7 = conn_7.cursor()
    c_7.execute("SELECT * from stats_two")
    data = c_7.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Yamada_calculations(batting_DB, batting_D, batting_T, batting_C, batting_G, RBI_to_hit_ratio_DB,RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C, RBI_to_hit_ratio_G,Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G, win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G):
        win = [win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,
                            RBI_to_hit_ratio_G]
        Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,
                                Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
        Total_number_of_games_contribution_by_team = []

        for i in range(5):
            prob_4_4 = (batting[i] ** 4)
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            total_predicted_hit = (predicted_total_games_played * prob_4_1) + (
                        predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (
                                              predicted_total_games_played * prob_4_4 * 4)
            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (
                        prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
            Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))
        return (Total_number_of_games_contribution_by_team)


    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = data[15][1], data[15][2], data[15][4], data[15][5]
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = data[20][1], data[20][2], data[20][4], data[20][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[11][4], data[11][5]
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = data[16][1], data[16][2], data[16][4], data[16][5]
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = data[21][1], data[21][2], data[21][4], data[21][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = data[17][1], data[17][2], data[17][4], data[17][5]
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = data[22][1], data[22][2], data[22][4], data[22][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = data[18][1], data[18][2], data[18][4], data[18][5]
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = data[23][1], data[23][2], data[23][4], data[23][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = data[19][1], data[19][2], data[19][4], data[19][5]
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = data[24][1], data[24][2], data[24][4], data[24][5]

    batting_DB_5 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB)
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB)
    RBI_to_hit_ratio_DB_5 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB_5 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB + homerun_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D)
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D)
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    RBI_to_hit_ratio_D_5 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D_5 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D + homerun_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T)
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T)
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    RBI_to_hit_ratio_T_5 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T_5 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T + homerun_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C)
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C)
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    RBI_to_hit_ratio_C_5 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C_5 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C + homerun_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G)
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G)
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)
    RBI_to_hit_ratio_G_5 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G_5 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G + homerun_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_4_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[1][2] + data_win[7][2] +data_win[13][2] + data_win[19][2])
    win_percentage_5_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1] + data_win[1][2] +data_win[7][2] + data_win[13][2] + data_win[19][2] + data_win[25][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_4_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[2][2] + data_win[8][2] +data_win[14][2] + data_win[20][2])
    win_percentage_5_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1] + data_win[2][2] +data_win[8][2] + data_win[14][2] + data_win[20][2] + data_win[26][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_4_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[3][2] + data_win[9][2] +data_win[15][2] + data_win[21][2])
    win_percentage_5_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1] + data_win[3][2] +data_win[9][2] + data_win[15][2] + data_win[21][2] + data_win[27][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_4_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[4][2] + data_win[10][2] + data_win[16][2] + data_win[22][2])
    win_percentage_5_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1] + data_win[4][2] + data_win[10][2] + data_win[16][2] + data_win[22][2] + data_win[28][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])
    win_percentage_4_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[5][2] + data_win[11][2] + data_win[17][2] + data_win[23][2])
    win_percentage_5_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1] + data_win[5][2] + data_win[11][2] + data_win[17][2] + data_win[23][2] + data_win[29][2])

    if year == 5:
        x = Yamada_calculations(batting_DB_5, batting_D_5, batting_T_5, batting_C_5, batting_G_5,
                                  RBI_to_hit_ratio_DB_5, RBI_to_hit_ratio_D_5, RBI_to_hit_ratio_T_5,
                                  RBI_to_hit_ratio_C_5, RBI_to_hit_ratio_G_5, Homerun_to_hit_ratio_DB_5,
                                  Homerun_to_hit_ratio_D_5, Homerun_to_hit_ratio_T_5, Homerun_to_hit_ratio_C_5,
                                  Homerun_to_hit_ratio_G_5, win_percentage_5_DB, win_percentage_5_D, win_percentage_5_T,
                                  win_percentage_5_C, win_percentage_5_G)
        print(x)
    elif year == 4:
        x = Yamada_calculations(batting_DB_4, batting_D_4, batting_T_4, batting_C_4, batting_G_4,
                                  RBI_to_hit_ratio_DB_4, RBI_to_hit_ratio_D_4, RBI_to_hit_ratio_T_4,
                                  RBI_to_hit_ratio_C_4, RBI_to_hit_ratio_G_4, Homerun_to_hit_ratio_DB_4,
                                  Homerun_to_hit_ratio_D_4, Homerun_to_hit_ratio_T_4, Homerun_to_hit_ratio_C_4,
                                  Homerun_to_hit_ratio_G_4, win_percentage_4_DB, win_percentage_4_D, win_percentage_4_T,
                                  win_percentage_4_C, win_percentage_4_G)
        print(x)
    elif year == 3:
        x = Yamada_calculations(batting_DB_3, batting_D_3, batting_T_3, batting_C_3, batting_G_3,
                                  RBI_to_hit_ratio_DB_3, RBI_to_hit_ratio_D_3, RBI_to_hit_ratio_T_3,
                                  RBI_to_hit_ratio_C_3, RBI_to_hit_ratio_G_3, Homerun_to_hit_ratio_DB_3,
                                  Homerun_to_hit_ratio_D_3, Homerun_to_hit_ratio_T_3, Homerun_to_hit_ratio_C_3,
                                  Homerun_to_hit_ratio_G_3, win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T,
                                  win_percentage_3_C, win_percentage_3_G)
        print(x)


    conn_7.commit()
    conn_7.close()
    conn_14.commit()
    conn_14.close()

def Santana(year):
    conn_8 = sqlite3.connect('Santana_stats_by_team.db')
    c_8 = conn_8.cursor()
    c_8.execute("SELECT * from stats_three")
    data = c_8.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Santana_calculations(batting_DB, batting_D, batting_T, batting_C, batting_G, RBI_to_hit_ratio_DB,RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C, RBI_to_hit_ratio_G,Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G, win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G):
        win = [win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,RBI_to_hit_ratio_G]
        Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
        Total_number_of_games_contribution_by_team = []

        for i in range(5):
            prob_4_4 = (batting[i] ** 4)
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun_DB = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
            Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))
        return (Total_number_of_games_contribution_by_team)


    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = data[15][1], data[15][2], data[15][4], data[15][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[11][4], data[11][5]
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = data[16][1], data[16][2], data[16][4], data[16][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = data[17][1], data[17][2], data[17][4], data[17][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = data[18][1], data[18][2], data[18][4], data[18][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = data[19][1], data[19][2], data[19][4], data[19][5]

    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB)
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB_4 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D)
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D_4 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)

    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T)
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T_4 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)

    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C)
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C_4 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)

    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G)
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G_4 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
                data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_4_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]) / (
                data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[1][2] + data_win[7][2] +
                data_win[13][2] + data_win[19][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
                data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_4_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]) / (
                data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[2][2] + data_win[8][2] +
                data_win[14][2] + data_win[20][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
                data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_4_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]) / (
                data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[3][2] + data_win[9][2] +
                data_win[15][2] + data_win[21][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
                data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_4_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]) / (
                data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[4][2] + data_win[10][
            2] + data_win[16][2] + data_win[22][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
                data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])
    win_percentage_4_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]) / (
                data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[5][2] + data_win[11][
            2] + data_win[17][2] + data_win[23][2])

    if year == 4:
        x = Santana_calculations(batting_DB_4, batting_D_4, batting_T_4, batting_C_4, batting_G_4, RBI_to_hit_ratio_DB_4, RBI_to_hit_ratio_D_4, RBI_to_hit_ratio_T_4, RBI_to_hit_ratio_C_4, RBI_to_hit_ratio_G_4, Homerun_to_hit_ratio_DB_4, Homerun_to_hit_ratio_D_4, Homerun_to_hit_ratio_T_4, Homerun_to_hit_ratio_C_4, Homerun_to_hit_ratio_G_4, win_percentage_4_DB, win_percentage_4_D, win_percentage_4_T, win_percentage_4_C, win_percentage_4_G)
        print(x)
    elif year == 3:
        x = Santana_calculations(batting_DB_3, batting_D_3, batting_T_3, batting_C_3, batting_G_3, RBI_to_hit_ratio_DB_3, RBI_to_hit_ratio_D_3, RBI_to_hit_ratio_T_3, RBI_to_hit_ratio_C_3, RBI_to_hit_ratio_G_3, Homerun_to_hit_ratio_DB_3, Homerun_to_hit_ratio_D_3, Homerun_to_hit_ratio_T_3, Homerun_to_hit_ratio_C_3, Homerun_to_hit_ratio_G_3, win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T, win_percentage_3_C, win_percentage_3_G)
        print(x)

    conn_8.commit()
    conn_8.close()
    conn_14.commit()
    conn_14.close()

def Osuna(year):
    conn_9 = sqlite3.connect('Osuna_stats_by_team.db')
    c_9 = conn_9.cursor()
    c_9.execute("SELECT * from stats_four")
    data = c_9.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Osuna_calculations(batting_DB, batting_D, batting_T, batting_C, batting_G, RBI_to_hit_ratio_DB,RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C, RBI_to_hit_ratio_G,Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G, win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G):
        win = [win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,RBI_to_hit_ratio_G]
        Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
        Total_number_of_games_contribution_by_team = []

        for i in range(5):
            prob_4_4 = (batting[i] ** 4)
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun_DB = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (
                        prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
            Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))
        return (Total_number_of_games_contribution_by_team)


    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = data[15][1], data[15][2], data[15][4], data[15][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[11][4], data[11][5]
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = data[16][1], data[16][2], data[16][4], data[16][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = data[17][1], data[17][2], data[17][4], data[17][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = data[18][1], data[18][2], data[18][4], data[18][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = data[19][1], data[19][2], data[19][4], data[19][5]

    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB)
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB_4 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D)
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D_4 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)

    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T)
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T_4 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)

    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C)
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C_4 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)

    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G)
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G_4 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
            data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_4_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]) / (
            data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[1][2] + data_win[7][2] +
            data_win[13][2] + data_win[19][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
            data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_4_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]) / (
            data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[2][2] + data_win[8][2] +
            data_win[14][2] + data_win[20][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
            data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_4_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]) / (
            data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[3][2] + data_win[9][2] +
            data_win[15][2] + data_win[21][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
            data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_4_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]) / (
            data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[4][2] + data_win[10][
        2] + data_win[16][2] + data_win[22][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
            data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])
    win_percentage_4_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]) / (
            data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[5][2] + data_win[11][
        2] + data_win[17][2] + data_win[23][2])

    if year == 4:
        x = Osuna_calculations(batting_DB_4, batting_D_4, batting_T_4, batting_C_4, batting_G_4,
                                 RBI_to_hit_ratio_DB_4, RBI_to_hit_ratio_D_4, RBI_to_hit_ratio_T_4,
                                 RBI_to_hit_ratio_C_4, RBI_to_hit_ratio_G_4, Homerun_to_hit_ratio_DB_4,
                                 Homerun_to_hit_ratio_D_4, Homerun_to_hit_ratio_T_4, Homerun_to_hit_ratio_C_4,
                                 Homerun_to_hit_ratio_G_4, win_percentage_4_DB, win_percentage_4_D, win_percentage_4_T,
                                 win_percentage_4_C, win_percentage_4_G)
        print(x)
    elif year == 3:
        x = Osuna_calculations(batting_DB_3, batting_D_3, batting_T_3, batting_C_3, batting_G_3,
                                 RBI_to_hit_ratio_DB_3, RBI_to_hit_ratio_D_3, RBI_to_hit_ratio_T_3,
                                 RBI_to_hit_ratio_C_3, RBI_to_hit_ratio_G_3, Homerun_to_hit_ratio_DB_3,
                                 Homerun_to_hit_ratio_D_3, Homerun_to_hit_ratio_T_3, Homerun_to_hit_ratio_C_3,
                                 Homerun_to_hit_ratio_G_3, win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T,
                                 win_percentage_3_C, win_percentage_3_G)
        print(x)

    conn_9.commit()
    conn_9.close()

def Aoki(year):
    conn_10 = sqlite3.connect('Aoki_stats_by_team.db')
    c_10 = conn_10.cursor()
    c_10.execute("SELECT * from stats_five")
    data = c_10.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Aoki_calculations(batting_DB, batting_D, batting_T, batting_C, batting_G, RBI_to_hit_ratio_DB,RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C, RBI_to_hit_ratio_G,Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G, win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G):
        win = [win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,RBI_to_hit_ratio_G]
        Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
        Total_number_of_games_contribution_by_team = []

        for i in range(5):
            prob_4_4 = (batting[i] ** 4)
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun_DB = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (
                    prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
            Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))
        return (Total_number_of_games_contribution_by_team)


    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = data[15][1], data[15][2], data[15][4], data[15][5]
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = data[20][1], data[20][2], data[20][4], data[20][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[11][4], data[11][5]
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = data[16][1], data[16][2], data[16][4], data[16][5]
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = data[21][1], data[21][2], data[21][4], data[21][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = data[17][1], data[17][2], data[17][4], data[17][5]
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = data[22][1], data[22][2], data[22][4], data[22][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = data[18][1], data[18][2], data[18][4], data[18][5]
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = data[23][1], data[23][2], data[23][4], data[23][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = data[19][1], data[19][2], data[19][4], data[19][5]
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = data[24][1], data[24][2], data[24][4], data[24][5]

    batting_DB_5 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB)
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB)
    RBI_to_hit_ratio_DB_5 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB_5 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB + homerun_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D)
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D)
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    RBI_to_hit_ratio_D_5 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D_5 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D + homerun_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T)
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T)
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    RBI_to_hit_ratio_T_5 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T_5 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T + homerun_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C)
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C)
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    RBI_to_hit_ratio_C_5 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C_5 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C + homerun_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G)
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G)
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)
    RBI_to_hit_ratio_G_5 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G_5 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G + homerun_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
                data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_4_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]) / (
                data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[1][2] + data_win[7][2] +
                data_win[13][2] + data_win[19][2])
    win_percentage_5_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1]) / (
                data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1] + data_win[1][2] +
                data_win[7][2] + data_win[13][2] + data_win[19][2] + data_win[25][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
                data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_4_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]) / (
                data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[2][2] + data_win[8][2] +
                data_win[14][2] + data_win[20][2])
    win_percentage_5_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1]) / (
                data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1] + data_win[2][2] +
                data_win[8][2] + data_win[14][2] + data_win[20][2] + data_win[26][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
                data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_4_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]) / (
                data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[3][2] + data_win[9][2] +
                data_win[15][2] + data_win[21][2])
    win_percentage_5_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1]) / (
                data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1] + data_win[3][2] +
                data_win[9][2] + data_win[15][2] + data_win[21][2] + data_win[27][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
                data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_4_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]) / (
                data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[4][2] + data_win[10][
            2] + data_win[16][2] + data_win[22][2])
    win_percentage_5_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1]) / (
                data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1] + data_win[4][
            2] + data_win[10][2] + data_win[16][2] + data_win[22][2] + data_win[28][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
                data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])
    win_percentage_4_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]) / (
                data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[5][2] + data_win[11][
            2] + data_win[17][2] + data_win[23][2])
    win_percentage_5_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1]) / (
                data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1] + data_win[5][
            2] + data_win[11][2] + data_win[17][2] + data_win[23][2] + data_win[29][2])

    if year == 5:
        x = Aoki_calculations(batting_DB_5, batting_D_5, batting_T_5, batting_C_5, batting_G_5,
                                RBI_to_hit_ratio_DB_5, RBI_to_hit_ratio_D_5, RBI_to_hit_ratio_T_5,
                                RBI_to_hit_ratio_C_5, RBI_to_hit_ratio_G_5, Homerun_to_hit_ratio_DB_5,
                                Homerun_to_hit_ratio_D_5, Homerun_to_hit_ratio_T_5, Homerun_to_hit_ratio_C_5,
                                Homerun_to_hit_ratio_G_5, win_percentage_5_DB, win_percentage_5_D, win_percentage_5_T,
                                win_percentage_5_C, win_percentage_5_G)
        print(x)
    elif year == 4:
        x = Aoki_calculations(batting_DB_4, batting_D_4, batting_T_4, batting_C_4, batting_G_4,
                                RBI_to_hit_ratio_DB_4, RBI_to_hit_ratio_D_4, RBI_to_hit_ratio_T_4,
                                RBI_to_hit_ratio_C_4, RBI_to_hit_ratio_G_4, Homerun_to_hit_ratio_DB_4,
                                Homerun_to_hit_ratio_D_4, Homerun_to_hit_ratio_T_4, Homerun_to_hit_ratio_C_4,
                                Homerun_to_hit_ratio_G_4, win_percentage_4_DB, win_percentage_4_D, win_percentage_4_T,
                                win_percentage_4_C, win_percentage_4_G)
        print(x)
    elif year == 3:
        x = Aoki_calculations(batting_DB_3, batting_D_3, batting_T_3, batting_C_3, batting_G_3,
                                RBI_to_hit_ratio_DB_3, RBI_to_hit_ratio_D_3, RBI_to_hit_ratio_T_3,
                                RBI_to_hit_ratio_C_3, RBI_to_hit_ratio_G_3, Homerun_to_hit_ratio_DB_3,
                                Homerun_to_hit_ratio_D_3, Homerun_to_hit_ratio_T_3, Homerun_to_hit_ratio_C_3,
                                Homerun_to_hit_ratio_G_3, win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T,
                                win_percentage_3_C, win_percentage_3_G)
        print(x)

    conn_10.commit()
    conn_10.close()
    conn_14.commit()
    conn_14.close()

def Shiomi(year):
    conn_11 = sqlite3.connect('Shiomi_stats_by_team.db')
    c_11 = conn_11.cursor()
    c_11.execute("SELECT * from stats_six")
    data = c_11.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    def Shiomi_calculations(batting_DB, batting_D, batting_T, batting_C, batting_G, RBI_to_hit_ratio_DB,RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C, RBI_to_hit_ratio_G,Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G, win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G):
        win = [win_percentage_DB, win_percentage_D, win_percentage_T, win_percentage_C, win_percentage_G]
        batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
        RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,RBI_to_hit_ratio_G]
        Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
        Total_number_of_games_contribution_by_team = []

        for i in range(5):
            prob_4_4 = (batting[i] ** 4)
            prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
            prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
            prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

            predicted_total_games_played = 22
            total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
            total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
            total_predicted_homerun_DB = total_predicted_hit * Homerun_to_hit_ratio[i]

            f = RBI_to_hit_ratio[i]

            Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (
                    prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
            Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))
        return (Total_number_of_games_contribution_by_team)


    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]
    bat_2021_DB, hit_2021_DB, homerun_2021_DB, RBI_2021_DB = data[15][1], data[15][2], data[15][4], data[15][5]
    bat_2020_DB, hit_2020_DB, homerun_2020_DB, RBI_2020_DB = data[20][1], data[20][2], data[20][4], data[20][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[11][4], data[11][5]
    bat_2021_D, hit_2021_D, homerun_2021_D, RBI_2021_D = data[16][1], data[16][2], data[16][4], data[16][5]
    bat_2020_D, hit_2020_D, homerun_2020_D, RBI_2020_D = data[21][1], data[21][2], data[21][4], data[21][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]
    bat_2021_T, hit_2021_T, homerun_2021_T, RBI_2021_T = data[17][1], data[17][2], data[17][4], data[17][5]
    bat_2020_T, hit_2020_T, homerun_2020_T, RBI_2020_T = data[22][1], data[22][2], data[22][4], data[22][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]
    bat_2021_C, hit_2021_C, homerun_2021_C, RBI_2021_C = data[18][1], data[18][2], data[18][4], data[18][5]
    bat_2020_C, hit_2020_C, homerun_2020_C, RBI_2020_C = data[23][1], data[23][2], data[23][4], data[23][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]
    bat_2021_G, hit_2021_G, homerun_2021_G, RBI_2021_G = data[19][1], data[19][2], data[19][4], data[19][5]
    bat_2020_G, hit_2020_G, homerun_2020_G, RBI_2020_G = data[24][1], data[24][2], data[24][4], data[24][5]

    batting_DB_5 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB + bat_2020_DB)
    batting_DB_4 = (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB + bat_2021_DB)
    batting_DB_3 = (hit_2024_DB + hit_2023_DB + hit_2022_DB) / (bat_2024_DB + bat_2023_DB + bat_2022_DB)
    RBI_to_hit_ratio_DB_5 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB + RBI_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    RBI_to_hit_ratio_DB_4 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB + RBI_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    RBI_to_hit_ratio_DB_3 = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB_5 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB + homerun_2020_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB + hit_2020_DB)
    Homerun_to_hit_ratio_DB_4 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB + homerun_2021_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB + hit_2021_DB)
    Homerun_to_hit_ratio_DB_3 = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)

    batting_D_5 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D + bat_2020_D)
    batting_D_4 = (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D) / (bat_2024_D + bat_2023_D + bat_2022_D + bat_2021_D)
    batting_D_3 = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    RBI_to_hit_ratio_D_5 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D + RBI_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    RBI_to_hit_ratio_D_4 = (RBI_2024_D + RBI_2023_D + RBI_2022_D + RBI_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    RBI_to_hit_ratio_D_3 = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D_5 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D + homerun_2020_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D + hit_2020_D)
    Homerun_to_hit_ratio_D_4 = (homerun_2024_D + homerun_2023_D + homerun_2022_D + homerun_2021_D) / (hit_2024_D + hit_2023_D + hit_2022_D + hit_2021_D)
    Homerun_to_hit_ratio_D_3 = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)

    batting_T_5 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T + bat_2020_T)
    batting_T_4 = (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T) / (bat_2024_T + bat_2023_T + bat_2022_T + bat_2021_T)
    batting_T_3 = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    RBI_to_hit_ratio_T_5 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T + RBI_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    RBI_to_hit_ratio_T_4 = (RBI_2024_T + RBI_2023_T + RBI_2022_T + RBI_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    RBI_to_hit_ratio_T_3 = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T_5 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T + homerun_2020_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T + hit_2020_T)
    Homerun_to_hit_ratio_T_4 = (homerun_2024_T + homerun_2023_T + homerun_2022_T + homerun_2021_T) / (hit_2024_T + hit_2023_T + hit_2022_T + hit_2021_T)
    Homerun_to_hit_ratio_T_3 = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)

    batting_C_5 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C + bat_2020_C)
    batting_C_4 = (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C) / (bat_2024_C + bat_2023_C + bat_2022_C + bat_2021_C)
    batting_C_3 = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    RBI_to_hit_ratio_C_5 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C + RBI_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    RBI_to_hit_ratio_C_4 = (RBI_2024_C + RBI_2023_C + RBI_2022_C + RBI_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    RBI_to_hit_ratio_C_3 = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C_5 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C + homerun_2020_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C + hit_2020_C)
    Homerun_to_hit_ratio_C_4 = (homerun_2024_C + homerun_2023_C + homerun_2022_C + homerun_2021_C) / (hit_2024_C + hit_2023_C + hit_2022_C + hit_2021_C)
    Homerun_to_hit_ratio_C_3 = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)

    batting_G_5 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G + bat_2020_G)
    batting_G_4 = (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G) / (bat_2024_G + bat_2023_G + bat_2022_G + bat_2021_G)
    batting_G_3 = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)
    RBI_to_hit_ratio_G_5 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G + RBI_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    RBI_to_hit_ratio_G_4 = (RBI_2024_G + RBI_2023_G + RBI_2022_G + RBI_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    RBI_to_hit_ratio_G_3 = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G_5 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G + homerun_2020_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G + hit_2020_G)
    Homerun_to_hit_ratio_G_4 = (homerun_2024_G + homerun_2023_G + homerun_2022_G + homerun_2021_G) / (hit_2024_G + hit_2023_G + hit_2022_G + hit_2021_G)
    Homerun_to_hit_ratio_G_3 = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (
            data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_4_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1]) / (
            data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[1][2] + data_win[7][2] +
            data_win[13][2] + data_win[19][2])
    win_percentage_5_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1]) / (
            data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[19][1] + data_win[25][1] + data_win[1][2] +
            data_win[7][2] + data_win[13][2] + data_win[19][2] + data_win[25][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (
            data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_4_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1]) / (
            data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[2][2] + data_win[8][2] +
            data_win[14][2] + data_win[20][2])
    win_percentage_5_D = (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1]) / (
            data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[20][1] + data_win[26][1] + data_win[2][2] +
            data_win[8][2] + data_win[14][2] + data_win[20][2] + data_win[26][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (
            data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_4_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1]) / (
            data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[3][2] + data_win[9][2] +
            data_win[15][2] + data_win[21][2])
    win_percentage_5_T = (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1]) / (
            data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[21][1] + data_win[27][1] + data_win[3][2] +
            data_win[9][2] + data_win[15][2] + data_win[21][2] + data_win[27][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (
            data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_4_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1]) / (
            data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[4][2] + data_win[10][
        2] + data_win[16][2] + data_win[22][2])
    win_percentage_5_C = (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1]) / (
            data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[22][1] + data_win[28][1] + data_win[4][
        2] + data_win[10][2] + data_win[16][2] + data_win[22][2] + data_win[28][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (
            data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])
    win_percentage_4_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1]) / (
            data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[5][2] + data_win[11][
        2] + data_win[17][2] + data_win[23][2])
    win_percentage_5_G = (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1]) / (
            data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[23][1] + data_win[29][1] + data_win[5][
        2] + data_win[11][2] + data_win[17][2] + data_win[23][2] + data_win[29][2])

    if year == 5:
        x = Shiomi_calculations(batting_DB_5, batting_D_5, batting_T_5, batting_C_5, batting_G_5,
                              RBI_to_hit_ratio_DB_5, RBI_to_hit_ratio_D_5, RBI_to_hit_ratio_T_5,
                              RBI_to_hit_ratio_C_5, RBI_to_hit_ratio_G_5, Homerun_to_hit_ratio_DB_5,
                              Homerun_to_hit_ratio_D_5, Homerun_to_hit_ratio_T_5, Homerun_to_hit_ratio_C_5,
                              Homerun_to_hit_ratio_G_5, win_percentage_5_DB, win_percentage_5_D, win_percentage_5_T,
                              win_percentage_5_C, win_percentage_5_G)
        print(x)
    elif year == 4:
        x = Shiomi_calculations(batting_DB_4, batting_D_4, batting_T_4, batting_C_4, batting_G_4,
                              RBI_to_hit_ratio_DB_4, RBI_to_hit_ratio_D_4, RBI_to_hit_ratio_T_4,
                              RBI_to_hit_ratio_C_4, RBI_to_hit_ratio_G_4, Homerun_to_hit_ratio_DB_4,
                              Homerun_to_hit_ratio_D_4, Homerun_to_hit_ratio_T_4, Homerun_to_hit_ratio_C_4,
                              Homerun_to_hit_ratio_G_4, win_percentage_4_DB, win_percentage_4_D, win_percentage_4_T,
                              win_percentage_4_C, win_percentage_4_G)
        print(x)
    elif year == 3:
        x = Shiomi_calculations(batting_DB_3, batting_D_3, batting_T_3, batting_C_3, batting_G_3,
                              RBI_to_hit_ratio_DB_3, RBI_to_hit_ratio_D_3, RBI_to_hit_ratio_T_3,
                              RBI_to_hit_ratio_C_3, RBI_to_hit_ratio_G_3, Homerun_to_hit_ratio_DB_3,
                              Homerun_to_hit_ratio_D_3, Homerun_to_hit_ratio_T_3, Homerun_to_hit_ratio_C_3,
                              Homerun_to_hit_ratio_G_3, win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T,
                              win_percentage_3_C, win_percentage_3_G)
        print(x)

    conn_11.commit()
    conn_11.close()

def Nakamura(year):
    pass

def Nagaoka():
    conn_13 = sqlite3.connect('Nagaoka_stats_by_team.db')
    c_13 = conn_13.cursor()
    c_13.execute("SELECT * from stats_eight")
    data = c_13.fetchall()
    conn_14 = sqlite3.connect('Win_lose_by_opponent.db')
    c_14 = conn_14.cursor()
    c_14.execute("SELECT * from stats_win_lose")
    data_win = c_14.fetchall()

    bat_2024_DB, hit_2024_DB, homerun_2024_DB, RBI_2024_DB = data[0][1], data[0][2], data[0][4], data[0][5]
    bat_2023_DB, hit_2023_DB, homerun_2023_DB, RBI_2023_DB = data[5][1], data[5][2], data[5][4], data[5][5]
    bat_2022_DB, hit_2022_DB, homerun_2022_DB, RBI_2022_DB = data[10][1], data[10][2], data[10][4], data[10][5]

    bat_2024_D, hit_2024_D, homerun_2024_D, RBI_2024_D = data[1][1], data[1][2], data[1][4], data[1][5]
    bat_2023_D, hit_2023_D, homerun_2023_D, RBI_2023_D = data[6][1], data[6][2], data[6][4], data[6][5]
    bat_2022_D, hit_2022_D, homerun_2022_D, RBI_2022_D = data[11][1], data[11][2], data[10][4], data[11][5]

    bat_2024_T, hit_2024_T, homerun_2024_T, RBI_2024_T = data[2][1], data[2][2], data[2][4], data[2][5]
    bat_2023_T, hit_2023_T, homerun_2023_T, RBI_2023_T = data[7][1], data[7][2], data[7][4], data[7][5]
    bat_2022_T, hit_2022_T, homerun_2022_T, RBI_2022_T = data[12][1], data[12][2], data[12][4], data[12][5]

    bat_2024_C, hit_2024_C, homerun_2024_C, RBI_2024_C = data[3][1], data[3][2], data[3][4], data[3][5]
    bat_2023_C, hit_2023_C, homerun_2023_C, RBI_2023_C = data[8][1], data[8][2], data[8][4], data[8][5]
    bat_2022_C, hit_2022_C, homerun_2022_C, RBI_2022_C = data[13][1], data[13][2], data[13][4], data[13][5]

    bat_2024_G, hit_2024_G, homerun_2024_G, RBI_2024_G = data[4][1], data[4][2], data[4][4], data[4][5]
    bat_2023_G, hit_2023_G, homerun_2023_G, RBI_2023_G = data[9][1], data[9][2], data[9][4], data[9][5]
    bat_2022_G, hit_2022_G, homerun_2022_G, RBI_2022_G = data[14][1], data[14][2], data[14][4], data[14][5]


    batting_DB = (hit_2024_DB + hit_2023_DB + hit_2022_DB)/(bat_2024_DB + bat_2023_DB + bat_2022_DB)
    batting_D = (hit_2024_D + hit_2023_D + hit_2022_D) / (bat_2024_D + bat_2023_D + bat_2022_D)
    batting_T = (hit_2024_T + hit_2023_T + hit_2022_T) / (bat_2024_T + bat_2023_T + bat_2022_T)
    batting_C = (hit_2024_C + hit_2023_C + hit_2022_C) / (bat_2024_C + bat_2023_C + bat_2022_C)
    batting_G = (hit_2024_G + hit_2023_G + hit_2022_G) / (bat_2024_G + bat_2023_G + bat_2022_G)

    RBI_to_hit_ratio_DB = (RBI_2024_DB + RBI_2023_DB + RBI_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    Homerun_to_hit_ratio_DB = (homerun_2024_DB + homerun_2023_DB + homerun_2022_DB) / (hit_2024_DB + hit_2023_DB + hit_2022_DB)
    RBI_to_hit_ratio_D = (RBI_2024_D + RBI_2023_D + RBI_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    Homerun_to_hit_ratio_D = (homerun_2024_D + homerun_2023_D + homerun_2022_D) / (hit_2024_D + hit_2023_D + hit_2022_D)
    RBI_to_hit_ratio_T = (RBI_2024_T + RBI_2023_T + RBI_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    Homerun_to_hit_ratio_T = (homerun_2024_T + homerun_2023_T + homerun_2022_T) / (hit_2024_T + hit_2023_T + hit_2022_T)
    RBI_to_hit_ratio_C = (RBI_2024_C + RBI_2023_C + RBI_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    Homerun_to_hit_ratio_C = (homerun_2024_C + homerun_2023_C + homerun_2022_C) / (hit_2024_C + hit_2023_C + hit_2022_C)
    RBI_to_hit_ratio_G = (RBI_2024_G + RBI_2023_G + RBI_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)
    Homerun_to_hit_ratio_G = (homerun_2024_G + homerun_2023_G + homerun_2022_G) / (hit_2024_G + hit_2023_G + hit_2022_G)

    batting = [batting_DB, batting_D, batting_T, batting_C, batting_G]
    RBI_to_hit_ratio = [RBI_to_hit_ratio_DB, RBI_to_hit_ratio_D, RBI_to_hit_ratio_T, RBI_to_hit_ratio_C,RBI_to_hit_ratio_G]
    Homerun_to_hit_ratio = [Homerun_to_hit_ratio_DB, Homerun_to_hit_ratio_D, Homerun_to_hit_ratio_T,Homerun_to_hit_ratio_C, Homerun_to_hit_ratio_G]
    Total_number_of_games_contribution_by_team = []

    win_percentage_3_DB = (data_win[1][1] + data_win[7][1] + data_win[13][1]) / (data_win[1][1] + data_win[7][1] + data_win[13][1] + data_win[1][2] + data_win[7][2] + data_win[13][2])
    win_percentage_3_D = (data_win[2][1] + data_win[8][1] + data_win[14][1]) / (data_win[2][1] + data_win[8][1] + data_win[14][1] + data_win[2][2] + data_win[8][2] + data_win[14][2])
    win_percentage_3_T = (data_win[3][1] + data_win[9][1] + data_win[15][1]) / (data_win[3][1] + data_win[9][1] + data_win[15][1] + data_win[3][2] + data_win[9][2] + data_win[15][2])
    win_percentage_3_C = (data_win[4][1] + data_win[10][1] + data_win[16][1]) / (data_win[4][1] + data_win[10][1] + data_win[16][1] + data_win[4][2] + data_win[10][2] + data_win[16][2])
    win_percentage_3_G = (data_win[5][1] + data_win[11][1] + data_win[17][1]) / (data_win[5][1] + data_win[11][1] + data_win[17][1] + data_win[5][2] + data_win[11][2] + data_win[17][2])

    win = [win_percentage_3_DB, win_percentage_3_D, win_percentage_3_T, win_percentage_3_C, win_percentage_3_G]

    for i in range(5):
        prob_4_4 = (batting[i] ** 4)
        prob_4_3 = (batting[i] ** 3) * (1 - batting[i]) * 4
        prob_4_2 = (batting[i] ** 2) * ((1 - batting[i]) ** 2) * 6
        prob_4_1 = (batting[i]) * ((1 - batting[i]) ** 3) * 4

        predicted_total_games_played = 22
        total_predicted_hit = (predicted_total_games_played * prob_4_1) + (predicted_total_games_played * prob_4_2 * 2) + (predicted_total_games_played * prob_4_3 * 3) + (predicted_total_games_played * prob_4_4 * 4)
        total_predicted_RBI = total_predicted_hit * RBI_to_hit_ratio[i]
        total_predicted_homerun_DB = total_predicted_hit * Homerun_to_hit_ratio[i]

        f = RBI_to_hit_ratio[i]

        Total_number_of_games_contribution = ((prob_4_1 * f) + (prob_4_2 * (1 - (1 - f) ** 2)) + (
                prob_4_3 * (1 - (1 - f) ** 3)) + (prob_4_4 * (1 - (1 - f) ** 4))) * predicted_total_games_played
        Total_number_of_games_contribution_by_team.append(int(Total_number_of_games_contribution * win[i]))

    print(Total_number_of_games_contribution_by_team)
    conn_13.commit()
    conn_13.close()


calculation('player 1', 5)
Nagaoka()

result_1 = Label(Results_page, text="The probability of the player hitting 0 hits out of 4 at bat in a game next season is")
result_1.pack()
result_2 = Label(Results_page, text="The probability of the player hitting 1 hits out of 4 at bat in a game next season is")
result_2.pack()
result_3 = Label(Results_page, text="The probability of the player hitting 2 hits out of 4 at bat in a game next season is")
result_3.pack()
result_4 = Label(Results_page, text="The probability of the player hitting 3 hits out of 4 at bat in a game next season is")
result_4.pack()
result_5 = Label(Results_page, text="The probability of the player hitting 3 hits out of 4 at bat in a game next season is")
result_5.pack()
back_btn = Button(Results_page, text='Back', command=lambda: confirmation_page.tkraise())
back_btn.pack()
calculate_btn = Button(Results_page, text='calculate')
calculate_btn.pack()

step = Label(instruction_page, text="Step by step instruction for the system")
step.grid(row=0, column=0)
step_three = Label(instruction_page, text="1. Click the start button on the start page.")
step_three.grid(row=1, column=0)
step_four = Label(instruction_page, text="2. Choose the player that you want the prediction of.")
step_four.grid(row=2, column=0)
step_five = Label(instruction_page, text="3. To find more information about the player and their stats, click on the button next to the name.")
step_five.grid(row=3, column=0)
step_six = Label(instruction_page, text="4. Choose the number of years of data the system want to use.")
step_six.grid(row=4, column=0)
step_seven = Label(instruction_page, text="5. The player's performance is displayed and its future too.")
step_seven.grid(row=5, column=0)
back_btn = Button(instruction_page, text='Back', command=lambda: start_page.tkraise())
back_btn.grid(row=6, column=0)

root.mainloop()
