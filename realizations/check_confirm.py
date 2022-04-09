from flask import request
import sqlite3


def check_confirm():
    user_id = request.args.get('user_id')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        c.execute(f"SELECT proof FROM Users WHERE id =?", (user_id,))
        data = c.fetchone()

        if data == None:
            return "Error"

    except sqlite3.IntegrityError:
        return "Error"
    return str(data[0])
