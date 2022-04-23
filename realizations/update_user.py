from flask import request
import sqlite3
from utility.hash_pass import hash_pwd
from log.logger import log_error

def update_user_by_id():
    user_id = request.args.get('id')
    username = request.args.get('name', default=None)
    date = request.args.get('birth', default=None)
    sex = request.args.get('sex', default=None)
    horoscope_id = request.args.get('sign', default=None)
    google = request.args.get('google', default=None)
    facebook = request.args.get('facebook', default=None)
    mail = request.args.get('mail', default=None)
    password = request.args.get('password', default=None)
    proof = 1
    print(username, date, sex, horoscope_id, mail, password)
    code = "confirmed by fb or google"
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        if username is not None:
            c.execute(f"UPDATE Users SET user_name=? WHERE id=?", (username, user_id))
        if date is not None:
            c.execute(f"UPDATE Users SET date_of_birth=? WHERE id=?", (date, user_id))
        if sex is not None:
            c.execute(f"UPDATE Users SET sex=? WHERE id=?", (sex, user_id))
        if horoscope_id is not None:
            c.execute(f"UPDATE Users SET horoscope_sign=? WHERE id=?", (horoscope_id, user_id))
        if google is not None:
            c.execute(f"UPDATE Users SET google_id=? WHERE id=?", (google, user_id))
        if facebook is not None:
            c.execute(f"UPDATE Users SET facebook_id=? WHERE id=?", (facebook, user_id))
        if mail is not None:
            c.execute(f"UPDATE Users SET mail=? WHERE id=?", (mail, user_id))
        if password is not None:
            password = hash_pwd(password)
            c.execute(f"UPDATE Users SET password=? WHERE id=?", (password, user_id))
        conn.commit()
        return str(c.lastrowid)

    except Exception as e:
        log_error(str(e), "update_user_by_id")
        return ("exception")
