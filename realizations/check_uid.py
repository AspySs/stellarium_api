from flask import request
import sqlite3
from log.logger import log_error, log_full

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
            log_full("User with google_id:facebook_id=" + str(uid)+":"+ str(uid2) + " Not found", "check_uid")
            return "Error"

    except Exception as e:
        log_error(str(e), "check_uid")
        return "Error"
    if (data[6] == None):
        return "f" + data[7]
    else:
        return "g" + data[6]
