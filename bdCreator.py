import sqlite3

from colorama import Fore

def tables_check():
    # подключаемся к БД
    print(Fore.BLUE + "Создание БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    # подключили
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

    print(Fore.BLUE + "Создание таблицы с гороскопами today" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS today_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами next_day" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS next_day_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами week" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS week_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами month" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS month_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    print(Fore.BLUE + "Создание таблицы с гороскопами year" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS year_horoscopes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, love TEXT, common TEXT, health TEXT, business TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")

    print(Fore.BLUE + "Создание таблицы с гороскопами характеристика" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS character_horoscopes (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, charact TEXT, love TEXT, career TEXT )")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")

    print(Fore.BLUE + "Создание таблицы с картами таро" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS taro_cards (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pic_name TEXT, desc_one_card TEXT, desc_day_card TEXT, desc_first_of_three_cards TEXT, desc_second_of_three_cards TEXT, desc_third_of_three_cards TEXT, desc_first_of_four_cards TEXT, desc_second_of_four_cards TEXT, desc_third_of_four_cards TEXT, desc_fourth_of_four_cards TEXT, desc_first_of_seven_cards TEXT, desc_second_of_seven_cards TEXT, desc_third_of_seven_cards TEXT, desc_fourth_of_seven_cards TEXT, desc_fifth_of_seven_cards TEXT, desc_sixth_of_seven_cards TEXT, desc_seventh_of_seven_cards TEXT)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")

    print(Fore.BLUE + "Создание таблицы лунного календаря" + " \n")
    c.execute("CREATE TABLE IF NOT EXISTS moon_calendar (date TEXT PRIMARY KEY NOT NULL, phase TEXT NOT NULL, characteristics TEXT NOT NULL, health TEXT NOT NULL, relations TEXT NOT NULL, business TEXT NOT NULL)")
    conn.commit()
    print(Fore.BLUE + "Успешно!" + " \n")
    #создали