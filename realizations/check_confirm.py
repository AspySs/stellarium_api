from flask import request
import sqlite3
from log.logger import log_error, log_full

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
            log_full("User with id="+str(user_id)+" Not found", "check_confirm")
            return "Error"

    except Exception as e:
        log_error(str(e), "check_confirm")
        return "Error"
    return str(data[0])
