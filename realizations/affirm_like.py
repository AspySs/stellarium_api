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

    c.execute("INSERT INTO liked_affirm ")