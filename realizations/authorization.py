from flask import request
import sqlite3

def auth_realization():
    google = request.args.get('google', default = None)
    facebook = request.args.get('facebook', default = None)
    mail = request.args.get('mail', default = None)
    password = request.args.get('password', default = None)
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        if(google != None):
            c.execute(f"SELECT * FROM Users WHERE google_id =?", (google, ))
            data = c.fetchone()
            if(data == None):
                return "False"
        elif(facebook != None):
            c.execute(f"SELECT * FROM Users WHERE facebook_id =?", (facebook, ))
            data = c.fetchone()
            if(data == None):
                return "False"
        elif((mail != None ) and (password != None)):
            c.execute(f"SELECT * FROM Users WHERE mail = ? AND password=?", (mail, password))
            data = c.fetchone()
            if(data == None):
                return "False"

        output = {
            "user": {
                "id": data[0],
                "name": data[2],
                "date": data[3],
                "sex": data[4],
                "sign": data[5],
                "mail_confirm": data[10]
            }
        }
        return output

    except sqlite3.IntegrityError:
        return "False"
    return "False"
