import sqlite3
from flask import request




def horo_comp_realization():
    first_id = int(request.args.get('first'))
    second_id = int(request.args.get('second'))
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    columns = ['love_text', 'sex_text', 'marriage_text', 'friend_text', 'love_val', 'sex_val', 'marriage_val', 'friend_val']
    data = []
    for i in columns:
        sql = "SELECT " + i + " FROM comp_horo WHERE first_sign_id = ? AND sec_sign_id = ?"
        c.execute(sql, (first_id, second_id))
        temp = c.fetchone()
        data.append(temp[0])
    output = {
        "compatibilityHoros": {
            "love_text": data[0],
            "sex_text": data[1],
            "marriage_text": data[2],
            "friend_text": data[3],
            "love_val": data[4],
            "sex_val": data[5],
            "marriage_val": data[6],
            "friend_val": data[7]
        }
    }
    return output


