import sqlite3
from colorama import Fore
from flask import request




def name_comp_realization():
    first_name = str(request.args.get('first'))
    second_name = str(request.args.get('second'))
    # подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    # подключили
    c.execute(f"SELECT MAX(id) FROM comp_names")
    max_index = c.fetchone()
    sum = 0
    for i in first_name:
        sum = sum + ord(i)
    for i in second_name:
        sum = sum + ord(i)
    hsh = (sum + len(first_name) + len(second_name) - ord(first_name[0]) - ord(second_name[0]))%max_index[0]
    if (hsh == 0):
        hsh = 1
    columns = ['love_text', 'friend_text', 'job_text', 'love_val', 'friend_val', 'job_val']
    data = []
    for i in columns:
        sql = "SELECT " + i + " FROM comp_names WHERE id = ?"
        c.execute(sql, (hsh, ))
        temp = c.fetchone()
        data.append(temp[0])
    output = {
        "compatibilityNames": {
            "love_text": data[0],
            "friend_text": data[1],
            "job_text": data[2],
            "love_val": data[3],
            "friend_val": data[4],
            "job_val": data[5]
        }
    }
    return output


