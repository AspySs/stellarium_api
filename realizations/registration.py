from flask import request
import sqlite3
from colorama import Fore

def register_realization():
    username = request.args.get('name')
    date = request.args.get('birth')
    sex = request.args.get('sex')
    horoscope_id = request.args.get('sign')
    google = request.args.get('google', default = None)
    facebook = request.args.get('facebook', default = None)
    mail = request.args.get('mail', default = None)
    password = request.args.get('password', default = None)
    # подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    # подключили
    try:
        print(Fore.GREEN + "Добавление записи в бд...")
        add = c.execute(f"INSERT INTO Users (mail, user_name, date_of_birth, sex, horoscope_sign, google_id, facebook_id, password) VALUES( ?, ?, ?, ?, ?, ?, ?, ?)", (mail, username, date, sex, horoscope_id, google, facebook, password))
        conn.commit()
        return str(c.lastrowid)

    except sqlite3.IntegrityError:
        print(Fore.GREEN + "Добавление записи в бд закончено с ошибкой")
        print(Fore.YELLOW + "End Registration!")
        return "False"
