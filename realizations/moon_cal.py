import sqlite3
from flask import request

def moon_calendar_realization():
    date = request.args.get('date')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
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