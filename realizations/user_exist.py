from flask import request
import sqlite3


def user_is_exist():
    mail = request.args.get('mail')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    c.execute("SELECT count(*)>0 FROM Users WHERE mail=?", (mail,))
    req = c.fetchone()
    if(req[0]):
        return "True"
    return "False"