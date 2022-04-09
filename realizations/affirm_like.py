import random
import sqlite3
from flask import request
import json
from random import randint

def add_affirm_to_liked():
    user_id = request.args.get('user_id')
    affirm_id = request.args.get('affirm_id')

    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        c.execute("SELECT count(*)>0 FROM liked_affirm WHERE user_id = ? and affirm_id =?", (user_id, affirm_id))
        req = c.fetchone()
        if(not req[0]):
            c.execute("INSERT INTO liked_affirm (affirm_id, user_id) VALUES (?, ?)", (affirm_id, user_id))
            conn.commit()
        return "True"
    except Exception as e:
        return str(e)

def delete_affirm_from_liked():
    user_id = request.args.get('user_id')
    affirm_id = request.args.get('affirm_id')

    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    try:
        c.execute("SELECT count(*)>0 FROM liked_affirm WHERE user_id = ? and affirm_id =?", (user_id, affirm_id))
        req = c.fetchone()
        if(req):
            c.execute("DELETE FROM liked_affirm WHERE user_id = ? AND affirm_id = ?", (user_id, affirm_id))
            conn.commit()
        return "True"
    except Exception as e:
        return str(e)
def get_affirm_from_liked():
    user_id = request.args.get('user_id')

    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    c.execute("SELECT affirm_id FROM liked_affirm WHERE user_id=?", (user_id,))
    ids = c.fetchall()
    data = {}
    for i in ids:
        c.execute("SELECT text FROM Affirmations WHERE id=?", (i[0],))
        text = c.fetchone()
        c.execute("SELECT picture FROM Affirmations WHERE id=?", (i[0],))
        picture = c.fetchone()
        temp = {"id": str(i[0]), "text": str(text[0]), "picture": str(picture[0])}
        data["affirmation_"+str(i[0])] = temp
    js = json.dumps(data)
    return js

