import sqlite3
from colorama import Fore
from parse.horoscope_pars import parse
import os
import shutil



def update_horoscope_table():

    cur_path = os.path.dirname(__file__)
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    path = ["horo_txts/classic/", "horo_txts/char/"]

    files = ["main.txt", "business.txt", "health.txt", "love.txt"]
    signs = ["aries/", "taurus/", "gemini/", "cancer/", "leo/", "virgo/", "libra/", "scorpio/", "sagittarius/", "capricorn/", "aquarius/", "pisces/"]
    tables = ["today_horoscopes", "next_day_horoscopes", "week_horoscopes", "month_horoscopes", "year_horoscopes"]
    if(os.path.isfile(cur_path + "/" + path[0] + signs[0] + files[0])):
        for i in signs:
            shutil.rmtree(cur_path + "/" + path[0] + i)
            os.mkdir(cur_path + "/" + path[0] + i)
            # shutil.rmtree(cur_path + "/" + path[1] + i)
            # os.mkdir(cur_path + "/" + path[1] + i)


    #включать когда нужно подтянуть новые гороскопы
    parse()



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
    #id = 1
    # for sig in signs:
    #     for j in char_files:#"description.txt", "charact.txt", "love.txt", "career.txt"
    #         with open(cur_path + "/" + path[1] + sig + j, 'r') as file:
    #             for line in file:
    #                 string = string + line + "\n"
    #         data.append(string)
    #         string=""
    #
    #     c.execute("INSERT INTO character_horoscopes (id, description, charact, love, career) VALUES(?, ?, ?, ?, ?)", (id, data[0], data[1], data[2], data[3]))
    #     conn.commit()
    #     data.clear()
    #     id = id + 1
