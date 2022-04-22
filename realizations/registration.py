from flask import request
import sqlite3
import string
import secrets
from utility.mail import send_mail
from utility.hash_pass import hash_pwd
from log.logger import log_error

def register_realization():
    username = request.args.get('name', default = None)
    date = request.args.get('birth', default = None)
    sex = request.args.get('sex', default = None)
    horoscope_id = request.args.get('sign', default = None)
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
        if(password != None):
            password = hash_pwd(password)
        add = c.execute(f"INSERT INTO Users (mail, user_name, date_of_birth, sex, horoscope_sign, google_id, facebook_id, password, code, proof) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (mail, username, date, sex, horoscope_id, google, facebook, password, code, proof))
        conn.commit()
        if(proof == 0):
            send_mail(mail, code)
        return str(c.lastrowid)

    except Exception as e:
        log_error(str(e), "register_realization")
        return ("exception")
