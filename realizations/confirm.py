from flask import request
import sqlite3
from colorama import Fore

def code_confirm():
    code = request.args.get('code')
    # подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    # подключили
    try:
        c.execute("UPDATE Users SET proof = 1 WHERE code=?", (code, ))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Error"
    return "Success"
