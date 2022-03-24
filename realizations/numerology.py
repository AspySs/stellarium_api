from flask import request
import sqlite3

def numerology_realization():
    number = request.args.get('num')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    colum = ['general', 'dignities', 'disadvantages', 'fate']
    data = []
    for i in colum:
        sql = "SELECT " + i + " FROM numerologic WHERE number = ?"
        c.execute(sql, (number, ))
        temp = c.fetchone()
        data.append(temp[0])
    output = {
            "number": number,
            "general": data[0],
            "dignities": data[1],
            "disadvantages": data[2],
            "fate": data[3]
    }
    return output