from flask import request
import sqlite3
from colorama import Fore

def register_realization():
    print(Fore.YELLOW + "Start Registration!")
    username = request.args.get('name')
    print(Fore.YELLOW + "Name: " + username)
    date = request.args.get('birth')
    print(Fore.YELLOW + "Birth date: " + date)
    sex = request.args.get('sex')
    print(Fore.YELLOW + "Sex: " + date)
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db") # или :memory: чтобы сохранить в RAM
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    try:
        print(Fore.GREEN+ "Добавление записи в бд...")
        add = c.execute(f"INSERT INTO Users (sex, user_name, date_of_birth ) VALUES( ?, ?, ?)", (sex, username, date))
        conn.commit()

    except sqlite3.IntegrityError:
        print(Fore.GREEN + "Добавление записи в бд закончено с ошибкой")
        print(Fore.YELLOW + "End Registration!")
        return "Error"
    c.execute(f"SELECT MAX(id) FROM Users")
    id = c.fetchone()
    print(Fore.GREEN + "Добавление записи в бд закончено успешно")
    print(Fore.YELLOW + "End Registration!")
    return str(id[0])
