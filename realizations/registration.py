from flask import request
import sqlite3
from colorama import Fore
import string
import secrets
from utility.mail import send_mail

def register_realization():
    username = request.args.get('name')
    date = request.args.get('birth')
    sex = request.args.get('sex')
    horoscope_id = request.args.get('sign')
    google = request.args.get('google', default = None)
    facebook = request.args.get('facebook', default = None)
    mail = request.args.get('mail', default = None)
    password = request.args.get('password', default = None)
    proof = 1
    code = "confirmed by fb or google"
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили

    if(mail!=None and password!=None):
        proof = 0
        flag = True
        while(flag):
            letters_and_digits = string.ascii_letters + string.digits
            code = ''.join(secrets.choice(letters_and_digits) for i in range(30))
            c.execute(f"SELECT * FROM Users WHERE code=?", (code,))
            data = c.fetchone()
            if (data == None):
                flag = False

    try:
        print(Fore.GREEN + "Добавление записи в бд...")
        add = c.execute(f"INSERT INTO Users (mail, user_name, date_of_birth, sex, horoscope_sign, google_id, facebook_id, password, code, proof) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (mail, username, date, sex, horoscope_id, google, facebook, password, code, proof))
        conn.commit()
        print(Fore.GREEN + "Новый пользователь добавлен!")
        if(proof == 0):
            send_mail(mail, code)
        return str(c.lastrowid)

    except sqlite3.IntegrityError as e:
        print(Fore.RED + "Добавление записи в бд закончено с ошибкой")
        print(Fore.YELLOW + "End Registration!")
        return str(e)
