from flask import request
import sqlite3


def check_uid():
    uid = request.args.get('uid')
    uid2 = uid
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        c.execute(f"SELECT * FROM Users WHERE google_id=? OR facebook_id=?", (uid, uid2))
        data = c.fetchone()

        if data == None:
            return "Error"

    except sqlite3.IntegrityError:
        return "Error"
    if (data[6] == None):
        return "f" + data[7]
    else:
        return "g" + data[6]
