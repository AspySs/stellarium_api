from flask import request
import sqlite3
from colorama import Fore

def moon_calendar_realization():
    date = request.args.get('date')
    # подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    # подключили
    data = []
    types = ["phase", "characteristics", "health", "relations", "business"]
    for i in types:
        sql = "SELECT " + i + " FROM moon_calendar WHERE date = ?"
        c.execute(sql, (date,))
        data.append(c.fetchone()[0])
    answer = {
            "calendar": {
                "date": date,
                "phase": data[0],
                "characteristics":data[1],
                "health":data[2],
                "relations":data[3],
                "business":data[4]

        }
    }
    return answer