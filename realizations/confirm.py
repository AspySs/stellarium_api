from flask import request
import sqlite3
from log.logger import log_error

def code_confirm():
    code = request.args.get('code')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        c.execute("UPDATE Users SET proof = 1 WHERE code=?", (code, ))
        conn.commit()
    except Exception as e:
        log_error(str(e), "code_confirm")
        return "Error"
    return "Success"
