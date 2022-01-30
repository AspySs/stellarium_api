import random
from flask import Flask
from flask import request
import sqlite3
import colorama
from random import randint
from colorama import Fore, Back, Style
import bdCreator
import json
import pifagGen_table

bdCreator.tables_check()
#pifagGen_table.gener_info()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/', methods=['GET'])
def register():
    print(Fore.YELLOW + "Start Registration!")
    username = request.args.get('name')
    print(Fore.YELLOW + "Name: " + username)
    date = request.args.get('birth')
    print(Fore.YELLOW + "Birth date: " + date)
    sex = request.args.get('sex')
    print(Fore.YELLOW + "Sex: " + date)
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db") # или :memory: чтобы сохранить в RAM
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    try:
        print(Fore.GREEN+ "Добавление записи в бд...")
        add = c.execute(f"INSERT INTO Users (sex, user_name, date_of_birth ) VALUES( ?, ?, ?)", (sex, username, date))
        conn.commit()

    except sqlite3.IntegrityError:
        print(Fore.GREEN + "Добавление записи в бд закончено с ошибкой")
        print(Fore.YELLOW + "End Registration!")
        return "Error"
    c.execute(f"SELECT MAX(id) FROM Users")
    id = c.fetchone()
    print(Fore.GREEN + "Добавление записи в бд закончено успешно")
    print(Fore.YELLOW + "End Registration!")
    return str(id[0])

@app.route('/test/', methods=['GET'])
def test():
    id = request.args.get('id')
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    c.execute(f"SELECT user_name FROM Users WHERE id="+id)
    name = c.fetchone()
    c.execute(f"SELECT sex FROM Users WHERE id="+id)
    sex = c.fetchone()
    c.execute(f"SELECT date_of_birth FROM Users WHERE id="+id)
    date_of_birth = c.fetchone()
    output = {
        "user": {
            "id": str(id),
            "name": str(name[0]),
            "sex": str(sex[0]),
            "date_of_birth": str(date_of_birth[0])
        }
    }
    print(Fore.GREEN + "Вывод данных о юзере закончен успешно")
    return output


@app.route('/affirmation/', methods=['GET'])
def affirm():
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

@app.route('/pifagorSquare/', methods=['GET'])
def pifagor():
    day = int(request.args.get('day'))
    month = int(request.args.get('month'))
    year = int(request.args.get('year'))

    firstWorkNumber = day//10 + day%10 + month//10 + month%10 + year//1000 + ((year//100)%10) + ((year%100)//10) + (year%10)
    secondWorkNumber =  firstWorkNumber//10 + firstWorkNumber%10
    thirdWorkNumber = (firstWorkNumber - 2)* (day//10)
    fourthWorkNumber = thirdWorkNumber//10 + thirdWorkNumber%10
    resultStr = str(day) + str(month) + str(year) + str(firstWorkNumber) + str(secondWorkNumber) + str(thirdWorkNumber) + str(fourthWorkNumber)
    result = list(range(0,10))
    for i in range(0,len(result)):
        result[i] = resultStr.count(str(i))
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    text = []
    sql = "SELECT text FROM pifagor_square WHERE num = ? AND num_count = ?"
    for i in range(1, 10):
        c.execute(sql, (i, result[i]))
        text0 = c.fetchall()
        text.append(text0[0])
    output = {
        "1": {
            "count": result[1],
            "text": text[0]
        },
        "2": {
            "count": result[2],
            "text": text[1]
        },
        "3": {
            "count": result[3],
            "text": text[2]
        },
        "4": {
            "count": result[4],
            "text": text[3]
        },
        "5": {
            "count": result[5],
            "text": text[4]
        },
        "6": {
            "count": result[6],
            "text": text[5]
        },
        "7": {
            "count": result[7],
            "text": text[6]
        },
        "8": {
            "count": result[8],
            "text": text[7]
        },
        "9": {
            "count": result[9],
            "text": text[8]
        }
    }
    return output

if __name__ == '__main__':
    app.run()
