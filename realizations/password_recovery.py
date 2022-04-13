from flask import request
import sqlite3
from colorama import Fore
import string
import secrets
from utility.mail import send_mail_pas_rec

def pass_rec():
    id = request.args.get('id')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    letters_and_digits = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(letters_and_digits) for i in range(30))
    passw = ''.join(secrets.choice(letters_and_digits) for i in range(15))

    c.execute(f"SELECT * FROM Users WHERE id=?", (id,))
    data = c.fetchone()
    if (data == None):
        return "User not found!"
    else:
        c.execute(f"SELECT mail FROM Users WHERE id=?", (id,))
        mail = c.fetchone()
    try:
        c.execute("UPDATE Users SET pass_recovery_code=? WHERE id=?", (code, id))
        conn.commit()
        c.execute("UPDATE Users SET temp_pass=? WHERE id=?", (passw, id))
        conn.commit()
        send_mail_pas_rec(mail[0], code, id, passw)
    except Exception as e:
        return str(e)

    return "True"

def activate_pass_rec():
    id = request.args.get('id')
    code = request.args.get('code')
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили

    c.execute(f"SELECT * FROM Users WHERE id=? AND pass_recovery_code=?", (id,code))
    data = c.fetchone()
    if (data == None):
        return "User not found!"

    try:
        c.execute("SELECT temp_pass FROM Users WHERE id=?", (id,))
        passw = c.fetchone()
        c.execute("UPDATE Users SET password=? WHERE id=? AND pass_recovery_code=?", (passw[0], id, code))
        conn.commit()
    except Exception as e:
        return str(e)

    return "Temp password is activated!"
