from flask import request
import sqlite3

def code_confirm():
    code = request.args.get('code')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        c.execute("UPDATE Users SET proof = 1 WHERE code=?", (code, ))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Error"
    return "Success"
