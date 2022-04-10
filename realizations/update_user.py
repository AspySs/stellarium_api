from flask import request
import sqlite3
from colorama import Fore


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
        print(Fore.GREEN + "Обновление записи в бд...")
        # add = c.execute(
        #     f"UPDATE Users SET (mail, user_name, date_of_birth, sex, horoscope_sign, google_id, facebook_id, password, code, proof) = ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE id = ?",
        #     (mail, username, date, sex, horoscope_id, google, facebook, password, code, proof, user_id))
        c.execute(
            f"UPDATE Users SET mail = ?, user_name=?, date_of_birth=?, sex=?, horoscope_sign=?, google_id=?, facebook_id=?, password=?, proof=? WHERE id=?",
            (mail, username, date, sex, horoscope_id, google, facebook, password, proof, user_id))
        conn.commit()
        print(Fore.GREEN + "Пользователь обновлен!")
        return str(c.lastrowid)

    except sqlite3.IntegrityError as e:
        print(Fore.RED + "Обновление записи в бд закончено с ошибкой")
        print(Fore.YELLOW + "End updating!")
        return str(e)
