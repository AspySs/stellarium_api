import random
import sqlite3
from flask import request
from random import randint

def add_affirm_to_liked():
    user_id = request.args.get('user_id')
    affirm_id = request.args.get('affirm_id')

    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    c.execute("INSERT INTO liked_affirm (affirm_id, user_id) VALUES (?, ?)", (affirm_id, user_id))
    conn.commit()

def delete_affirm_from_liked():
    user_id = request.args.get('user_id')
    affirm_id = request.args.get('affirm_id')

    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    c.execute("DELETE FROM liked_affirm WHERE user_id = ? AND affirm_id = ?", (user_id, affirm_id))
    conn.commit()

def get_affirm_from_liked():
    user_id = request.args.get('user_id')

    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    c.execute("SELECT affirm_id FROM liked_affirm WHERE user_id=?", (user_id,))
    ids = c.fetchall()
    #мене пихуй, потом сделаю
