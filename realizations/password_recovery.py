from flask import request
import sqlite3
from colorama import Fore
from utility.hash_pass import hash_pwd
import string
import secrets
from utility.mail import send_mail_pas_rec

def pass_rec():
    mail = request.args.get('mail')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    letters_and_digits = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(letters_and_digits) for i in range(30))
    passw = ''.join(secrets.choice(letters_and_digits) for i in range(15))

    c.execute(f"SELECT * FROM Users WHERE mail=?", (mail,))
    data = c.fetchone()
    if (data == None):
        return "User not found!"
    try:
        c.execute("UPDATE Users SET pass_recovery_code=? WHERE mail=?", (code, mail))
        conn.commit()
        passw_h = hash_pwd(passw)
        c.execute("UPDATE Users SET temp_pass=? WHERE mail=?", (passw_h, mail))
        conn.commit()
        send_mail_pas_rec(mail, code, mail, passw)
    except Exception as e:
        return ("exception")

    return "True"


def activate_pass_rec():
    mail = request.args.get('mail')
    code = request.args.get('code')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили

    c.execute(f"SELECT * FROM Users WHERE mail=? AND pass_recovery_code=?", (mail, code))
    data = c.fetchone()
    if (data == None):
        return "User not found!"

    try:
        c.execute("SELECT temp_pass FROM Users WHERE mail=?", (mail,))
        passw = c.fetchone()
        c.execute("UPDATE Users SET password=? WHERE mail=? AND pass_recovery_code=?", (passw[0], mail, code))
        conn.commit()
    except Exception as e:
        return str(e)

    return "Temp password is activated!"


def update_password():
    id = request.args.get('id')
    new_pass = request.args.get('passwordN')
    old_pass = request.args.get('passwordO')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили

    c.execute(f"SELECT * FROM Users WHERE id=?", (id, ))
    data = c.fetchone()
    if (data == None):
        return "User not found!"

    try:
        new_pass = hash_pwd(new_pass)
        old_pass = hash_pwd(old_pass)
        c.execute("UPDATE Users SET password=? WHERE id=? AND password=?", (new_pass, id, old_pass))
        conn.commit()
    except Exception as e:
        return str(e)

    return "Password successful updated!"
