import random
from flask import request
import sqlite3
from random import randint
from colorama import Fore

def affirmations_realization():
    user_id = request.args.get('id')
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    c.execute(f"SELECT MAX(id) FROM Affirmations")
    max = c.fetchone()
    c.execute(f"SELECT MAX(affirm_id) FROM Affirmations_shown WHERE user_id="+user_id)
    if (c.fetchone() is None):
        af_id = randint(1, max[0])
    else:
        c.execute(f"SELECT affirm_id FROM Affirmations_shown WHERE user_id="+user_id)
        except_nums = c.fetchall()
        ran_nums = list(range(1, max[0]+1))
        for i in range(0, len(except_nums)):
            ran_nums.remove(except_nums[i][0])
        try:
            af_id = random.choice(ran_nums)
        except IndexError:
            c.execute(f"DELETE FROM Affirmations_shown WHERE user_id="+user_id)
            conn.commit()
            print("Not enough affirmations to show, restart table")
            af_id = randint(1, max[0])
    c.execute(f"SELECT text FROM Affirmations WHERE id=" + str(af_id))
    text = c.fetchone()
    c.execute(f"SELECT picture FROM Affirmations WHERE id=" + str(af_id))
    pic = c.fetchone()
    affirmation = {
        "affirmation": {
            "id": af_id,
            "text": text[0],
            "picture": pic[0]
        }
    }
    c.execute(f"INSERT INTO Affirmations_shown (user_id, affirm_id) VALUES( ?, ?)", (user_id, af_id))
    conn.commit()
    return affirmation
