import sqlite3
import colorama
from colorama import Fore, Back, Style

def tables_check():
    #создаем базу данных
    print(Fore.BLUE + "Создание БД...." + " \n")
    conn = sqlite3.connect('stell.db')
    c = conn.cursor()
    print(Fore.BLUE + "Создание таблицы с юзерами" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, mail TEXT UNIQUE, user_name TEXT, date_of_birth DATE, sex BOOLEAN, horoscope_sign INTEGER)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с аффирмациями" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS Affirmations (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, text TEXT, picture BLOB)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с показанными аффирмациями" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS Affirmations_shown (user_id INTEGER PRIMARY KEY, affirm_id INTEGER)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с квадратом пифагора" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS pifagor_square (num INTEGER, num_count INTEGER, text TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    #создали