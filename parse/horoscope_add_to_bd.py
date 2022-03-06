import sqlite3
from colorama import Fore
from parse.horoscope_pars import parse
import os



def update_horoscope_table():
    parse()
    cur_path = os.path.dirname(__file__)
    # подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    # подключили
    path = ["horo_txts/classic/", "horo_txts/char/"]
    files = ["main.txt", "business.txt", "health.txt", "love.txt"]
    char_files = ["description.txt", "charact.txt", "love.txt", "career.txt"]
    signs = ["capricorn/", "taurus/", "virgo/", "aquarius/", "gemini/", "libra/", "pisces/", "cancer/", "scorpio/", "aries/", "leo/", "sagittarius/"]
    tables = ["today_horoscopes", "next_day_horoscopes", "week_horoscopes", "month_horoscopes", "year_horoscopes", "character_horoscopes"]
    # 1 - capricorn
    # 2 - taurus
    # 3 - virgo
    # 4 - aquarius
    # 5 - gemini
    # 6 - libra
    # 7 - pisces
    # 8 - cancer
    # 9 - scorpio
    # 10 - aries
    # 11 - leo
    # 12 - sagittarius
    #очистка
    for i in tables:
        sql = "DELETE FROM "+i+";"
        c.execute(sql)
        conn.commit()


    data = []
    string = ""
    id = 1

    #считываю данные из файлов и пихаю в бд
    for sig in signs:
        for j in files:#"main", "business", "health", "love"
            with open(cur_path + "/" + path[0] + sig + "today_" + j, 'r') as file:
                for line in file:
                    string = string + line + "\n"
            data.append(string)
            string=""
        c.execute("INSERT INTO today_horoscopes (id, common, business, health, love) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
        conn.commit()
        data.clear()

        for j in files:
            with open(cur_path + "/" + path[0] + sig + "tomorrow_" + j, 'r') as file:
                for line in file:
                    string = string + line + "\n"
            data.append(string);
            string=""
        c.execute("INSERT INTO next_day_horoscopes (id, common, business, health, love) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
        conn.commit()
        data.clear()

        for j in files:
            with open(cur_path + "/" + path[0] + sig + "week_" + j, 'r') as file:
                for line in file:
                    string = string + line + "\n"
            data.append(string);
            string=""
        c.execute("INSERT INTO week_horoscopes (id, common, business, health, love) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
        conn.commit()
        data.clear()

        for j in files:
            with open(cur_path + "/" + path[0] + sig + "month_" + j, 'r') as file:
                for line in file:
                    string = string + line + "\n"
            data.append(string);
            string=""
        c.execute("INSERT INTO month_horoscopes (id, common, business, health, love) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
        conn.commit()
        data.clear()


        for j in files:
            with open(cur_path + "/" + path[0] + sig + "year_" + j, 'r') as file:
                for line in file:
                    string = string + line + "\n"
            data.append(string);
            string=""
        c.execute("INSERT INTO year_horoscopes (id, common, business, health, love) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
        conn.commit()
        data.clear()
        id = id+1
    id = 1
    for sig in signs:
        for j in char_files:#"description.txt", "charact.txt", "love.txt", "career.txt"
            with open(cur_path + "/" + path[1] + sig + j, 'r') as file:
                for line in file:
                    string = string + line + "\n"
            data.append(string)
            string=""

        c.execute("INSERT INTO character_horoscopes (id, description, charact, love, career) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
        conn.commit()
        data.clear()
        id = id + 1
